import datetime
from datetime import datetime
import pyowm


class Weather:
    def __init__(self, token, logger):
        self._weather_manager = None
        self._logger = logger
        self._token = token

    def get_weather_list(self, city: str):
        """This function gives information about the weather in the city
         for five days in advance every three hours
        in the form of a dictionary. """
        try:
            self._weather_manager = pyowm.OWM(self._token).weather_manager()
            weather_data = self._weather_manager.forecast_at_place(city, '3h').forecast
            date_list, weather = [], []
            for index in weather_data:
                date_list.append(
                    [datetime.fromtimestamp(index.ref_time).strftime('%Y-%m-%d %H:%M'),
                     index.humidity,
                     index.temperature('fahrenheit')['temp'],
                     index.temperature('fahrenheit')['temp_min'],
                     index.temperature('fahrenheit')['temp_max']])
            for index in date_list:
                weather.append(
                    {
                        'date': index[0],
                        'humidity': index[1],
                        'temp': index[2],
                        'temp_min': index[3],
                        'temp_max': index[4]
                    }
                )
        except Exception:
            self._logger.exception('Ошибка в работе с  API')
            raise
        return weather
