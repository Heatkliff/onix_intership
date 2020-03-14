from functools import reduce

global_var = 3  # Создать глобальную переменную


def second_task():  # Вынести задание предыдущего урока в самостоятельную функцию, не возвращающую ничего
    int_variable = 0  # Создать числовую переменную
    str_variable = ''  # создать переменную с типом строка
    print(type(int_variable) == type(str_variable))  # сравнить их типы
    int_variable = str(int_variable)  # конвертировать числовую переменную в строчную
    list_variable = [1, 0, 0, 0]  # Создать список
    print(list_variable)
    list_variable.append(12)  # добавить элемент в конец списка
    print(list_variable)
    list_variable.insert(3, 17)  # добавить элемент в нужную позицию в списке
    print(list_variable)
    list_variable.pop(0)  # удалить первый элемент
    print(list_variable)
    list_variable.pop(2)  # удалить элемент списка по индексу
    print(list_variable)
    list_variable.reverse()  # развернуть список
    print(len(list_variable))  # подсчитать количество элементов в списке
    new_list_variable = list_variable.copy()  # Сделать копию списка
    print(new_list_variable)
    # Сортировать первый список одним из алгоритмов сортировки
    # Пузырьковая сортировка
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(list_variable) - 1):
            if list_variable[i] > list_variable[i + 1]:
                list_variable[i], list_variable[i + 1] = list_variable[i + 1], list_variable[i]
                swapped = True
    new_list_variable.sort()  # Сортировать второй список одним из стандартных методов
    print(new_list_variable)
    '''
    list.sort() сортирует список и сохраняет отсортированный список, а sorted(list) возвращает отсортированный список 
    без изменения исходного списка.
    '''
    print(' '.join(
        sorted("This is a test string for Internship Onix for python".split())))  # Отсортировать строку по алфавиту
    dict_variable = {  # Создать словарь
        'name': 'Nick',
        'last_name': 'Koriak',
        'city': 'Kropyvnytskiy'
    }
    print(dict_variable)
    dict_variable['internship'] = 'Onix'  # добавить элемент в словарь
    print(dict_variable)
    print(dict_variable['name'])  # получить значение из словаря по ключу
    del (dict_variable['city'])  # удалить элемент из словаря
    print(dict_variable)
    print(dict_variable.keys())  # получить все ключи
    print(dict_variable.values())  # получить все значения
    # Сортировать словарь по ключам
    sorted_dict_by_key = {key_old: dict_variable[key_old] for key_old in sorted(dict_variable.keys())}
    print(sorted_dict_by_key)
    # Сортировать словарь по значениям
    sorted_dict_by_key = {key_old: dict_variable[key_old] for key_old in sorted(dict_variable, key=dict_variable.get)}
    print(sorted_dict_by_key)


# Создать функцию, которая будет принимать в себя числовую переменную
def increase_by_glob(returned_list, var_for_increase=0):
    returned_list.append(var_for_increase * global_var)  # умножать ее на глобальную и записывать в список
    return returned_list, len(returned_list)  # возвращать список и количество элементов в нем


# Создать функцию принимающую в себя *args, **kwargs
def get_args_kwargs(*args, **kwargs):
    print(f"args={args}\nkwargs={kwargs}")  # Функция должна выводить в консоль переданные переменные
    return True


def is_divisible_by(num, divisor):  # Написать функцию is_divisible_by(num, divisor),
    return num % divisor == 0  # которая будет проверять делится ли число num без остатка на divisor


def fibonacci(n):  # Написать функцию, которая будет считать числа фибоначчи
    if n in (1, 2):
        return 1
    elif n == 0:  # На случай если какой-то умный программист решит что первый элемент - нулевой
        return 1
    elif n < 0:  # На случай если кому-то нечем занятся и он пытается вызвать несуществующее число
        return False
    return fibonacci(n - 1) + fibonacci(n - 2)


class TaskTwoFirst:
    # Инициализировать класс, принимающий переменную number
    def __init__(self, number=0):
        print('cool')
        self.number = number

    # Объявить метод __del__ который будет выводить в консоль какой-то текст, когда объект класса будет удален
    def __del__(self):
        print('not cool')

    # Перенести метод is_divisible_by из прошлого задания в класс, принимающий переменную divisor
    def is_divisible_by(self, divisor):  # Написать функцию is_divisible_by(num, divisor),
        return self.number % divisor == 0  # которая будет проверять делится ли число num без остатка на divisor

    # Создать в классе статический метод
    @staticmethod
    def static_method(first_num, second_num):
        # В статическом методе создать lamba функцию, которая будет перемножать 2 числа, которые вы передадите в метод
        lambda_func = lambda l_first_num, l_second_num: l_first_num * l_second_num
        return lambda_func(first_num, second_num)


# Наследоваться от класса созданного ранее
class TaskTwoSecond(TaskTwoFirst):
    # Создать защищенную переменную внутри класса.
    _protected_var = 'aaa'

    # Создать приватный метод в новом классе который будет проверять является ли переменная строкой
    def __check_string(self, check_variable):  # private method
        return type(check_variable) == 'string'

    def run_private_method(self, check_variable):
        return self.__check_string(check_variable)


# Наследоваться от класса созданного ранее
class TaskTwoThird(TaskTwoSecond):

    # Переопределить статический метод родительского класса
    # Переопределенный статический метод должен вычислять НОК и НОД 2-ух переданных чисел
    @staticmethod
    def static_method(first_num, second_num):
        while first_num != 0 and second_num != 0:
            if first_num > second_num:
                first_num %= second_num
            else:
                second_num %= first_num
        gcd = first_num + second_num  # Наибольший общий делитель
        gcf = (first_num * second_num) / gcd
        print(gcd, gcf)
        return False


if __name__ == '__main__':
    # Задачи со второй недели
    second_task()

    # Задачи с третьей недели
    list_for_increase = []  # Список для записи через функцию increase_by_glob
    print(increase_by_glob(list_for_increase, 3))
    print(get_args_kwargs('test1', 'test2', 'test3', 'test4', test=1, test2=2, test3=3, test4=12))
    print(is_divisible_by(4, 2))
    print(fibonacci(-1))

    # Задачи с четвертой недели
    # Создать объект класса TaskTwo и вызвать функцию
    TaskTwo_obj = TaskTwoFirst(22)
    print(TaskTwo_obj.is_divisible_by(2))
    # Вызвать статический  метод в коде.
    TaskTwoFirst.static_method(2, 6)
    # Создать объект нового класса.
    TaskTwoSecond_obj = TaskTwoSecond(22)
    # Вызвать метод из родительского класса
    print(TaskTwoSecond_obj.static_method(6, 3))
    # вызвать приватный метод
    print(TaskTwoSecond_obj.run_private_method(32))
    # попробовать вызвать защищенную переменную
    print(TaskTwoSecond_obj._protected_var)
    # Создать объект нового класса
    TaskTwoThird_obj = TaskTwoThird()
    # вызвать метод
    print(TaskTwoThird.static_method(20, 10))

    # Use map to print the square of each numbers rounded
    # to two decimal places
    my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]
    # print(list(map(lambda float_var: round(float_var ** 2, 2), my_floats)))

    # Use filter to print only the names that are less than
    # or equal to seven letters
    my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]
    # print(list(filter(lambda str_var: len(str_var) <= 7, my_names)))

    # Use reduce to print the product of these numbers
    my_numbers = [4, 6, 9, 23, 5]
    # print(reduce(lambda num1, num2: num1 * num2, my_numbers))

    # Fix all three respectively.
    map_result = list(map(lambda x: round(x ** 2, 2), my_floats))
    filter_result = list(filter(lambda name: len(name) <= 7, my_names))
    reduce_result = reduce(lambda num1, num2: num1 * num2, my_numbers)

    print(map_result)
    print(filter_result)
    print(reduce_result)
