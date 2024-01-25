def get_factorial(number):
    """The function of finding the factorial of a number"""
    factorial = 1
    for index in range(2, number + 1):
        factorial *= index
    return factorial


def get_fibonacci(number):
    """Function for finding Fibonacci numbers"""
    final_fib, temp_fib = 1, 1
    for index in range(1, number+1):
        temp_fib, final_fib = final_fib, final_fib + temp_fib
    return final_fib


if __name__ == '__main__':
    print('Первичные значения 1 и 1 не учитываются при расчете.')
    numbers = 0
    required_input = True
    while required_input:
        try:
            numbers = int(input('Введите число для нахождения факториала и чисел Фибоначчи:'))
            if numbers < 1:
                raise IndexError
        except IndexError:
            print('Число не может быть отрицательным')
        except ValueError:
            print('Вводиться должно число')
        else:
            required_input = False
    factorials = get_factorial(numbers)
    for numbers_index in range(1, numbers+1):
        fibonacci = get_fibonacci(numbers_index)
        print(f'{numbers_index} итерация:  {fibonacci}')
    print(f'Выполнено {numbers} итераций. Факториал {numbers}! = {factorials}')
