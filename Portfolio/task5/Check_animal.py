import re
from Animal import Animal
import os


choice_dict = {1: '1) Вывести более подробную информацию о животном', 2: '2) Скорректировать информацию',
               3: '3) Сохранить и выйти', 4: '4) Выйти без сохранения'}
list_dict = {1: 'name', 2: 'gen', 3: 'view', 4: 'average_life_expectancy', 5: 'average_height',
             6: 'average_body_weight', 7: 'habitat', 8: 'country'}
choice_correct_dict = {1: '1) name', 2: '2) gen', 3: '3) view', 4: '4) average_life_expectancy', 5: '5) average_height',
                       6: '6) average_body_weight', 7: '7) habitat', 8: '8) country'}


def get_verify_letters(string, number_paragraph):
    if number_paragraph in (1, 2, 3, 7, 8):
        return bool(re.search('[а-яА-Я]', string))


def get_verify_numeric(string, number_paragraph):
    string = float(string)
    if number_paragraph in (4, 5, 6) and type(string) == float:
        return True


def get_list_animal(list_animal):
    print(f'{list_animal.name}\n{list_animal.gen}\n{list_animal.view}\n'
          f'Средняя продолжительность жизни: {list_animal.average_life_expectancy}\n'
          f'средний рост животного: {list_animal.average_height}\n'
          f'средняя масса тела: {list_animal.average_body_weight}\n'
          f'{list_animal.habitat}\n{list_animal.country}')


def get_new_line(number):
    require_input, new_line = True, ''
    if number in (1, 2, 3, 7, 8):
        while require_input:
            try:
                new_line = input('Введите новую строку: ')
                if get_verify_letters(new_line, number):
                    require_input = False
                else:
                    raise ValueError
            except ValueError:
                print('Здесь должны быть русские буквы')
    elif number in (4, 5, 6):
        while require_input:
            try:
                new_line = input('Введите новую строку: ')
                if get_verify_numeric(new_line, number):
                    require_input = False
                else:
                    raise ValueError
            except ValueError:
                print('Здесь должны быть цифры')
    return new_line


def set_list_animal(list_animal, paragraph, new_line):
    old_line = ''
    if paragraph == 'name':
        old_line = list_animal.name
        list_animal.name = new_line
    elif paragraph == 'gen':
        old_line = list_animal.gen
        list_animal.gen = new_line
    elif paragraph == 'view':
        old_line = list_animal.view
        list_animal.view = new_line
    elif paragraph == 'average_life_expectancy':
        old_line = list_animal.average_life_expectancy
        list_animal.average_life_expectancy = new_line
    elif paragraph == 'average_height':
        old_line = list_animal.average_height
        list_animal.average_height = new_line
    elif paragraph == 'average_body_weight':
        old_line = list_animal.average_body_weight
        list_animal.average_body_weight = new_line
    elif paragraph == 'habitat':
        old_line = list_animal.habitat
        list_animal.habitat = new_line
    elif paragraph == 'country':
        old_line = list_animal.country
        list_animal.country = new_line
    return old_line


def get_choice():
    for index in range(1, len(choice_dict) + 1):
        print(choice_dict[index])
    required_input, pick = True, 0
    while required_input:
        try:
            pick = int(input('Выберите действие: '))
            if pick not in (1, 2, 3, 4):
                raise ValueError
        except ValueError:
            print('Такого выбора не дано')
        else:
            required_input = False
    return pick


def get_animal(list_animal):
    for i in range(len(list_animal)):
        print(list_animal[i])


def get_list_class(path, animals_fail, name_animals):
    for index in range(len(animals_fail)):
        full_path = os.path.join(path, animals_fail[index])
        filename = open(full_path, "r", encoding='utf-8')
        list_inform = [line.strip() for line in filename.readlines()]
        name_animals[index] = Animal(list_inform[0], list_inform[1], list_inform[2], list_inform[3], list_inform[4],
                                     list_inform[5], list_inform[6], list_inform[7])


def get_animal_list(animals_fail, name_animals):
    choice_animal = get_choice_animal(animals_fail)
    for index in range(len(animals_fail)):
        if animals_fail[index] == choice_animal:
            get_list_animal(name_animals[index])


def get_adjustment(animals_fail, name_animals):
    new_line, old_line, paragraph_name = '', '', ''
    choice_animal = get_choice_animal(animals_fail)
    for index in range(len(animals_fail)):
        if animals_fail[index] == choice_animal:
            for i in range(1, len(choice_correct_dict) + 1):
                print(choice_correct_dict[i])
            list_choice_input = get_list_choice_input()
            paragraph_name = list_dict[list_choice_input]
            new_line = get_new_line(list_choice_input)
            old_line = set_list_animal(name_animals[index], paragraph_name, new_line)
    required_input, choice_correct = True, ''
    while required_input:
        try:
            choice_correct = input(f'Применить корректировки? (Да/Нет) Значение до: {old_line},'
                                   f' значение после: {new_line}: ')
            choice_correct = choice_correct.capitalize()
            if choice_correct not in ('Да', 'Нет'):
                raise ValueError
        except ValueError:
            print('Надо ввести либо "Да", либо "Нет"')
        else:
            required_input = False
    if choice_correct == 'Да':
        return False
    elif choice_correct == 'Нет':
        for index in range(len(animals_fail)):
            if animals_fail[index] == choice_animal + '.txt':
                set_list_animal(name_animals[index], paragraph_name, old_line)
        return True


def get_list_choice_input():
    required_input, choice_input = True, 0
    while required_input:
        try:
            choice_input = int(input('Выберите пункт для изменения: '))
            if choice_input not in range(1, 9):
                raise ValueError
        except ValueError:
            print('Ввели несуществующее действие')
        else:
            required_input = False
    return choice_input


def get_choice_animal(all_animals):
    required_input, choice_animal = True, ''
    while required_input:
        try:
            choice_animal = input('Выберите животное: ')+'.txt'
            choice_animal = choice_animal.capitalize()
            if choice_animal not in all_animals:
                raise ValueError
        except ValueError:
            print('В базе такого животного нет')
        else:
            required_input = False
    return choice_animal


def set_classes(path, objects, animals_fail):
    for index in range(len(objects)):
        full_path = os.path.join(path, animals_fail[index])
        fileread = open(full_path, "r", encoding='utf-8')
        list_inform = [line.strip() for line in fileread.readlines()]
        fileread.close()
        list_information = get_list_information(objects[index])
        file_correct = open(full_path, 'w', encoding='utf-8')
        for lines in range(len(list_inform)):
            temper = list_information[lines]
            list_inform[lines] = f'{temper}\n'
            file_correct.writelines(list_inform[lines])
        file_correct.close()


def get_list_information(information):
    list_information = [information.name, information.gen, information.view, information.average_life_expectancy,
                        information.average_height, information.average_body_weight, information.habitat,
                        information.country]
    return list_information
