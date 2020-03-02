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
