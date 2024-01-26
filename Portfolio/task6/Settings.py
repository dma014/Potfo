from configparser import ConfigParser
import os.path
import argparse
from json import load


class Settings:
    def __init__(self, settings, name_file):
        self._file = None
        self._list_city = None
        self._class_settings = None
        self._parser_settings = None
        self._args = None
        self._parser = None
        self._settings = {}
        self._name_settings = settings
        self._name_file = name_file

    def get_settings(self):
        """This function returns the settings from the file
         and the settings entered from the console"""
        self._parser = argparse.ArgumentParser()
        if os.path.exists(self._name_settings):
            self._class_settings = ConfigParser()
            self._class_settings.read(self._name_settings)
            for key in self._class_settings:
                self._settings.update(self._class_settings[key])
        else:
            raise FileNotFoundError
        self._parser = argparse.ArgumentParser()
        self._parser.add_argument('--database_schema', default='public')
        self._parser.add_argument('--database_table', default='weather')
        self._parser.add_argument('--logging', default='file')
        self._args = self._parser.parse_args()
        self._parser_settings = {'database_schema': self._args.database_schema,
                                 'database_table': self._args.database_table,
                                 'logging': self._args.logging}
        return self._settings, self._parser_settings

    def get_city_list(self):
        """This function reads Json file"""
        list_city = []
        try:
            file = open(self._name_file, 'r', encoding='utf-8')
            list_city = load(file)
            file.close()
        except FileNotFoundError:
            print('Такого файла не существует')
        return list_city
