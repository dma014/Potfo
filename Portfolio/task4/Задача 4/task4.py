import random
import logging
import os


filename = 'logs'
if not os.path.exists(filename):
    os.mkdir('logs')


logging.basicConfig(level='DEBUG', filename='logs/logs.log', format='%(asctime)s %(levelname)s:%(message)s')
logger = logging.getLogger()


def get_random(random_n, people_n, nums, comparisons):
    if 1 <= abs(random_n - people_n) <= 10:
        print('Жарко')
    elif 10 < abs(random_n - people_n) <= 20:
        print('Горячо')
    elif 20 < abs(random_n - people_n) <= 30:
        print('Тепло')
    else:
        print('Холодно')
    if nums != 1:
        print('Горячее' if random_n - comparisons > random_n - people_n else 'Холоднее')


if __name__ == '__main__':
    random_number = random.randint(1, 100)
    people_number = int(input('Введите случайное число от 1 до 100:'))
    if people_number not in range(1, 100):
        raise ValueError('Введено неверное число')
    logger.debug(f'Введено число: {people_number}')
    qty = 1
    comparison = 0
    if random_number == people_number:
        print('Вы угадали с первого раза')
    else:
        while random_number != people_number:
            get_random(random_number, people_number, qty, comparison)
            comparison = people_number
            people_number = int(input('Попробуйте еще раз:'))
            if people_number not in range(1, 100):
                raise ValueError('Введено неверное число')
            logger.debug(f'Введено число: {people_number}')
            qty += 1
            if random_number == people_number:
                print(f'Ура, вы выиграли c {qty} попытки')
