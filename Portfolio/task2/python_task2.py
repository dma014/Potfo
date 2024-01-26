import random
import sys


dict_horoscope = {0: 'обезьяны', 1: 'петуха', 2: 'собаки', 3: 'свиньи', 4: 'крысы', 5: 'быка',
                  6: 'тигра', 7: 'кролика', 8: 'дракона', 9: 'змеи', 10: 'лошади', 11: 'козы'}
dict_quarter = {1: '1 квартал', 2: '1 квартал', 3: '1 квартал', 4: '2 квартал', 5: '2 квартал', 6: '2 квартал',
                7: '3 квартал', 8: '3 квартал', 9: '3 квартал', 10: '4 квартал', 11: '4 квартал', 12: '4 квартал'}
dict_month = {1: 'Январь', 2: 'Февраль', 3: 'Март', 4: 'Апрель', 5: 'Май', 6: 'Июнь',
              7: 'Июль', 8: 'Август', 9: 'Сентябрь', 10: 'Октябрь', 11: 'Ноябрь', 12: 'Декабрь'}
dict_week = {0: 'Среда', 1: 'Четверг', 2: 'Пятница', 3: 'Суббота', 4: 'Воскресенье', 5: 'Понедельник', 6: 'Вторник'}
dict_day_of_week = {'Понедельник': 1, 'Вторник': 2, 'Среда': 3, 'Четверг': 4, 'Пятница': 5,
                    'Суббота': 6, 'Воскресенье': 7}
dict_day_of_year = {'Январь': 31, 'Февраль': 28, 'Март': 31, 'Апрель': 30, 'Май': 31, 'Июнь': 30,
                    'Июль': 31, 'Август': 31, 'Сентябрь': 30, 'Октябрь': 31, 'Ноябрь': 30, 'Декабрь': 31}
dict_number_of_year = {1: 31, 2: 28, 2.1: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}


def get_leap_year(leap_date):
    """function checks leap year or not"""
    if leap_date % 4 == 0 and ((leap_date % 100 != 0) or (leap_date % 400 == 0)):
        return True
    else:
        return False


def horoscope(horoscope_date):
    """The function determines the horoscope
     according to the Chinese calendar"""
    return horoscope_date % 12


def get_day(day_date, month_date, year_date):
    """The function indicates how many days have passed since the beginning of the year"""
    qty_day = 0
    for i in range(1, month_date):
        qty_day += dict_number_of_year[i]
    qty_day += day_date
    if year_date and month_date > 2:
        return qty_day+1
    return qty_day


def day_of_week(date_year, date_day_year):
    """Function that determines the day of the week"""
    week_day = date_day_year
    for index in range(1970, date_year):
        if not get_leap_year(index):
            week_day += 365
        else:
            week_day += 366
    return week_day % 7


if __name__ == '__main__':
    required_input = True
    day, month, year, date, leap_year = 0, 0, 0, 0, True
    if len(sys.argv) == 1:
        while required_input:
            try:
                date = str(input('Введите дату в формате - "dd.mm.yyyy":'))
                day = int(date[:2])
                month = int(date[3:5])
                year = int(date[6:10])
                temp_month = month
                if date[2] != '.' or date[5] != '.':
                    raise ValueError
                elif len(date) < 10:
                    raise IndexError
                elif month not in range(1, 13):
                    raise IndexError
                elif year not in range(1970, 2101):
                    raise IndexError
                leap_year = get_leap_year(year)
                if leap_year and month == 2:
                    temp_month = 2.1
                if day not in range(1, dict_number_of_year[temp_month]+1):
                    raise TypeError
            except ValueError:
                print('значения должны быть числовыми, формат ввода - "dd.mm.yyyy"')
            except TypeError:
                print('В этом месяце нет столько дней')
            except IndexError:
                print('месяц должен быть от 1 до 12, год должен быть от 1970 до 2100')
            else:
                required_input = False
    else:
        date = ''
        year = random.randint(1970, 2100)
        leap_year = get_leap_year(year)
        month = random.randint(1, 12)
        temp_month = month
        if leap_year and month == 2:
            temp_month = 2.1
        day = random.randint(1, dict_number_of_year[temp_month])
        if len(str(day)) < 2:
            date += '0'+str(day)+'.'
        else:
            date += str(day)+'.'
        if len(str(month)) < 2:
            date += '0'+str(month)+'.'
        else:
            date += str(month)+'.'
        date += str(year)
    if not leap_year:
        print(f'{date} - Обычный год (не високосный)')
    else:
        print(f'{date} - Високосный год')
    animal = horoscope(year)
    day_year = get_day(day, month, leap_year)
    week = day_of_week(year, day_year)
    print(f'{year} - год {dict_horoscope[animal]}')
    print(dict_quarter[month])
    print(f'{month} {dict_month[month]}')
    print(f'{dict_day_of_week[dict_week[week]]} день недели')
    print(f'{day_year} столько дней прошло с начала года')
    print(f'День недели {dict_week[week]}')
