import psycopg2
from psycopg2.sql import SQL, Identifier


class DataBase:
    def __init__(self, database_settings, parser_settings, logger):
        self._conn = None
        self._cur = None
        self._connect = None
        self._settings = database_settings
        self._database_schema = parser_settings['database_schema']
        self._database_table = parser_settings['database_table']
        self._logger = logger

    def get_database_connection(self):
        """This function connects to the database"""
        try:
            self._connect = psycopg2.connect(
                host=self._settings['host'],
                user=self._settings['user'],
                password=self._settings['password'],
                dbname=self._settings['db_name'],
                port=self._settings['port']
            )
        except psycopg2.OperationalError:
            self._logger.exception('Ошибка подключения к базе')
            raise
        return self._connect

    @staticmethod
    def get_weather_for_city(town: dict, weather: dict):
        """This function combines the information of the city and its weather"""
        data_city = {'city': town['name'], 'city_code': town['id']}
        weather_city = {**data_city, **weather}
        return weather_city

    def load_weather(self, weather_list, connection):
        """This function loads the weather information into the database"""
        self._conn = connection
        with self._conn:
            with self._conn.cursor() as curs:
                query = "INSERT INTO {}.{} (id, city, city_code, forecast_date, loadet_dt, humidity, temp, " \
                        "temp_min, temp_max) VALUES (DEFAULT, %s, %s, %s, DEFAULT, %s, %s, %s, %s) "
                weather = [weather_list['city'], weather_list['city_code'], weather_list['date'],
                           weather_list['humidity'],
                           weather_list['temp'], weather_list['temp_min'], weather_list['temp_max']]
                curs.execute(SQL(query).format(*map(Identifier,
                                                    (self._database_schema, self._database_table))), weather)

    def get_number_of_lines(self, connection):
        """This function returns the number of rows in a table"""
        self._conn = connection
        with self._conn:
            with self._conn.cursor() as curs:
                curs.execute(f"SELECT * FROM {self._database_schema}.{self._database_table}")
                return len(curs.fetchall())

    def get_connect_closed(self, connection):
        """This function closes the connection to the database"""
        self._conn = connection
        self._conn.commit()
        self._conn.close()

    @property
    def database_schema(self):
        return self._database_schema

    @database_schema.setter
    def database_schema(self, database_schema):
        self._database_schema = database_schema

    @property
    def database_table(self):
        return self._database_table

    @database_table.setter
    def database_table(self, database_table):
        self._database_table = database_table
