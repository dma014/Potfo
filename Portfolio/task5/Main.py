import os
import Check_animal


if __name__ == '__main__':
    catalog = 'animal_info'  # input('Введите путь к папке')
    list_name_animals_fail = os.listdir(catalog)
    list_name_animals = [i[:i.rfind('.')] for i in os.listdir(catalog)]
    Check_animal.get_animal(list_name_animals)
    required_input = True
    Check_animal.get_list_class(catalog, list_name_animals_fail, list_name_animals)
    while required_input:
        check_animal = True
        choice_input = Check_animal.get_choice()
        if choice_input == 1:
            Check_animal.get_animal_list(list_name_animals_fail, list_name_animals)
        elif choice_input == 2:
            while check_animal:
                check_animal = Check_animal.get_adjustment(list_name_animals_fail, list_name_animals)
        elif choice_input == 3:
            Check_animal.set_classes(catalog, list_name_animals, list_name_animals_fail)
            required_input = False
        elif choice_input == 4:
            required_input = False
