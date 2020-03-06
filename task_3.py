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
    list.sort() сортирует список и сохраняет отсортированный список, а sorted(list) возвращает отсортированный список без 
    изменения исходного списка.
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


# В конструкции name ==  ‘__main__’ вызвать все функции по порядку и вывести в консоль то, что они возвращают.
if __name__ == "__main__":
    second_task() # Задачи со второй недели
    list_for_increase = [] # Список для записи через функцию increase_by_glob
    print(increase_by_glob(list_for_increase, 3))
    print(get_args_kwargs('test1', 'test2', 'test3', 'test4', test=1, test2=2, test3=3, test4=12))
    print(is_divisible_by(4, 2))
    print(fibonacci(-1))
