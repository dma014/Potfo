import psycopg2

conn = psycopg2.connect("host = 127.0.0.1 dbname = postgres user = admin password = root port = 5432")

cur = conn.cursor()


def insert_into_city(cursor):
    cursor.execute("INSERT INTO city SELECT sale_city_code, sale_city, "
                   "TIMESTAMP'1700-01-01' as start_dt, TIMESTAMP'3000-01-01' as end_dt,"
                   " CURRENT_TIMESTAMP as loaded_dt,"
                   " sale_city_code"
                   "||'~'||sale_city"
                   "||'~'||TIMESTAMP'1700-01-01'"
                   "||'~'||TIMESTAMP'3000-01-01' as ccd "
                   "FROM ( SELECT sale_city, sale_city_code from stage "
                   "UNION SELECT client_city, client_city_code from stage) as city_and_code")


def insert_into_partners(cursor):
    cursor.execute("INSERT INTO partners SELECT partner_id, sale_city_code, partner_name,"
                   " TIMESTAMP'1700-01-01' as start_dt,"
                   " TIMESTAMP'3000-01-01' as end_dt,"
                   " CURRENT_TIMESTAMP as loaded_dt,"
                   " partner_id"
                   "||'~'||sale_city_code"
                   "||'~'||partner_name"
                   "||'~'||TIMESTAMP'1700-01-01'"
                   "||'~'||TIMESTAMP'3000-01-01' as ccd FROM stage")


def insert_into_product(cursor):
    cursor.execute("INSERT INTO product (reference_code, start_dt, end_dt, loaded_dt, ccd) "
                   "SELECT reference_code, start_dt, end_dt, loaded_dt, ccd "
                   "FROM(SELECT ROW_NUMBER() OVER(PARTITION BY reference_code ORDER BY reference_code) as row,"
                   " reference_code,"
                   " TIMESTAMP'1700-01-01' as start_dt,"
                   " TIMESTAMP'3000-01-01' as end_dt,"
                   " CURRENT_TIMESTAMP as loaded_dt,"
                   " reference_code"
                   "||'~'||TIMESTAMP'1700-01-01'"
                   "||'~'||TIMESTAMP'3000-01-01' as ccd FROM stage) as tmp_product WHERE row = 1")


def insert_into_client(cursor):
    cursor.execute("INSERT INTO client (client_city_code, inn_client, client_name, "
                   "client_category, start_dt, end_dt, loaded_dt, ccd) "
                   "SELECT client_city_code, inn_client, client_name, client_category,"
                   " TIMESTAMP'1700-01-01' as start_dt,"
                   " TIMESTAMP'3000-01-01' as end_dt,"
                   " CURRENT_TIMESTAMP as loaded_dt,"
                   " client_city_code"
                   "||'~'||inn_client"
                   "||'~'||client_name"
                   "||'~'||client_category"
                   "||'~'||TIMESTAMP'1700-01-01'"
                   "||'~'||TIMESTAMP'3000-01-01' as ccd FROM stage")


def insert_into_sales(cursor):
    cursor.execute("WITH tmp_product AS "
                   "(SELECT stage_id, product_id FROM product"
                   " INNER JOIN stage ON product.reference_code = stage.reference_code),"
                   " tmp_client AS"
                   " (SELECT stage_id, client_id FROM client"
                   " INNER JOIN stage ON client.inn_client = stage.inn_client),"
                   " tmp_partners AS"
                   " (SELECT stage_id, partners.partner_id FROM partners"
                   " INNER JOIN stage ON partners.partner_id = stage.partner_id),"
                   " tmp_stage AS (SELECT tmp_client.stage_id as stage_id, client_id,"
                   " partner_id, product_id FROM tmp_client INNER JOIN tmp_partners"
                   " ON tmp_client.stage_id = tmp_partners.stage_id INNER JOIN tmp_product"
                   " ON tmp_client.stage_id = tmp_product.stage_id)"
                   " INSERT INTO sales(partner_id, date_id, product_id, client_id, sold_qty,"
                   " purchase_price, loaded_dt, ccd)"
                   " SELECT stage.partner_id as partner_id, sold_date as date_id,"
                   " product_id, client_id, sold_qty, purchase_price, CURRENT_TIMESTAMP as loaded_dt,"
                   " stage.partner_id"
                   "||'~'||sold_date"
                   "||'~'||product_id"
                   "||'~'||client_id"
                   "||'~'||sold_qty"
                   "||'~'||purchase_price as ccd "
                   "FROM stage INNER JOIN tmp_stage ON stage.stage_id = tmp_stage.stage_id")


insert_into_city(cur)
insert_into_partners(cur)
insert_into_product(cur)
insert_into_client(cur)
insert_into_sales(cur)
conn.commit()
conn.close()
