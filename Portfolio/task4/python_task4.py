import random
import logging
import os
from datetime import datetime as dt
import time


date_today = time.strftime("%Y.%m.%d - %Hh %Mm %Ss")
filename = 'Logs'
if not os.path.exists(filename):
    os.mkdir('Logs')
date_name = os.path.join('Logs', f'python_task4.py {date_today}')
logging.basicConfig(level='INFO', filename=f'{date_name}.log')
logger = logging.getLogger()
dict_direction = {0: 'Невероятно жарко', 1: 'Очень жарко', 2: 'Жарко', 3: 'Тепло', 4: 'Тепленько',
                  5: 'прохладно', 6: 'Холодновато', 7: 'Холодно', 8: 'Очень холодно', 9: 'Невероятно холодно'}


def get_random(random_n, people_n, number, comparisons):
    direction = abs(random_n - people_n) // 10
    print(dict_direction[direction])
    if number != 1:
        print('Горячее' if abs(random_n - comparisons) > abs(random_n - people_n) else 'Холоднее')


if __name__ == '__main__':
    logger.info(f'Начало игры: {dt.now()}')
    people_number, qty, comparison = 0, 0, 0
    random_number = random.randint(1, 100)
    while random_number != people_number:
        required_input = True
        while required_input:
            try:
                people_number = int(input('Введите случайное число от 1 до 100:'))
                if people_number not in range(1, 101):
                    raise IndexError
            except ValueError:
                print('Должно быть число')
            except IndexError:
                print('вы вышли за рамки, число должно быть от 1 до 100')
            else:
                required_input = False
        logging.info(f'введеное число {people_number}')
        qty += 1
        if random_number == people_number:
            print(f'Вы угадали с {qty} раза')
            break
        get_random(random_number, people_number, qty, comparison)
        comparison = people_number
    logging.info(f'Конец игры: {dt.now()}')
    logging.info(f'Вы выиграли с {qty} попытки')
