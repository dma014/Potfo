def get_imt(person_weight, person_height):
    """Body mass index calculation function"""
    imt_body_tmp = person_weight / person_height ** 2
    print(imt_body_tmp)
    imt_body = round(imt_body_tmp, 1)
    return imt_body


def get_age(person_age):
    """Age Category Calculation Function"""
    if person_age <= 1:
        category = 'Младенец'
    elif 1 < person_age <= 10:
        category = 'Ребенок'
    elif 10 < person_age <= 18:
        category = 'Подросток'
    elif 18 < person_age <= 60:
        category = 'Взрослый'
    else:
        category = 'Пожилой'
    return category


if __name__ == '__main__':
    required_input = True
    height, weight, age, imt = 0, 0, 0, 0
    while required_input:
        try:
            information = list(map(str, input('Введите свой рост, вес, возраст через запятую:').split(',')))
            height = float(information[0])
            weight = int(information[1])
            age = int(information[2])
            if height > 4:
                height /= 100
            imt = get_imt(weight, height)
        except ValueError:
            print('Введенные значения должны быть цифровыми')
        except ZeroDivisionError:
            print('Рост не может быть равен 0')
        except IndexError:
            print('Вы ввели не все данные')
        else:
            required_input = False
    if imt <= 16:
        diagnosis = 'Выраженный дефицит массы тела'
    elif 16 < imt <= 18.5:
        diagnosis = 'Недостаточная(дифицит) масса тела'
    elif 18.5 < imt <= 25:
        diagnosis = 'Норма'
    elif 25 < imt <= 30:
        diagnosis = 'Избыточная масса тела(предожирение)'
    elif 30 < imt <= 35:
        diagnosis = 'Ожирение первой степени'
    elif 35 < imt <= 40:
        diagnosis = 'Ожирение второй степени'
    else:
        diagnosis = 'Ожирение третьей степени(морбидное)'
    print(f'Ваш ИМТ - {imt}({diagnosis})')
    age_category = get_age(age)
    print(f'Ваша возрастная категория - {age_category}')
