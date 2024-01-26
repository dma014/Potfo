import logging
import time
import os
import sys


class Logging:
    def __init__(self):
        self._logger = logging.getLogger()

    def get_file_handler(self, logg):
        """This function is responsible for creating the protocol"""
        if logg == 'stdout':
            stdout_handler = logging.StreamHandler(sys.stdout)
            self._logger.addHandler(stdout_handler)
            self._logger.setLevel(logging.INFO)
            return self._logger
        elif logg == 'file':
            date_today = time.strftime("%Y.%m.%d - %Hh %Mm %Ss")
            filename = 'logs'
            if not os.path.exists(filename):
                os.mkdir('logs')
            file_handler = logging.FileHandler(f'./logs/{date_today}.log', encoding='UTF-8')
            file_handler.setFormatter(logging.Formatter(f"%(asctime)s - [%(levelname)s] - %(name)s - %(message)s"))
            self._logger.addHandler(file_handler)
            self._logger.setLevel(logging.INFO)
            return self._logger
