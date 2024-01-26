from API import Weather
from Settings import Settings
from DataBase import DataBase
from Logging import Logging


if __name__ == '__main__':
    count_rows = 0
    path = 'settings.ini'
    name_file_city = 'city.list.json'
    main_settings = Settings(path, name_file_city)
    static_settings, console_settings = main_settings.get_settings()
    logging_type = console_settings['logging']
    api_key = static_settings['token']
    main_logger = Logging()
    logger = main_logger.get_file_handler(logging_type)
    logger.info('Начало программы')
    weather_manager = Weather(api_key, logger)
    city_list = main_settings.get_city_list()
    logger.info('Список городов получен')
    main_database = DataBase(static_settings, console_settings, logger)
    database_connect = main_database.get_database_connection()
    logger.info('Подключение к базе данных успешно')
    for city in city_list:
        weather_list = weather_manager.get_weather_list(city['name'])
        number_of_rows_to_load = main_database.get_number_of_lines(database_connect)
        for key in weather_list:
            weather_city = main_database.get_weather_for_city(city, key)
            main_database.load_weather(weather_city, database_connect)
        number_of_rows_after_load = main_database.get_number_of_lines(database_connect)
        count_rows = number_of_rows_after_load - number_of_rows_to_load
        logger.info(f'Информация о погоде в городе {city["name"]} загружено {count_rows} строк')
    logger.info('Все города загружены успешно')
    main_database.get_connect_closed(database_connect)
    logger.info('Отключение от базы данных успешно')
