# map - применяет одну функцию ко всем элемента списпка
"""
my_string = '1234567890'
my_string = list(map(int, my_string))
функция map переводит все эелменты строки в интовые значения
"""
# filter -
"""
def is_digit(num:str):
    return num.isdigit()
my_string = '1y2f34g56wery7890hh'
my_string = list(map(int,filter(int, my_string)))
функция map переводит все эелменты строки в интовые значения
функция filter отсеивает в данном случае буквы и оставляет цифры
"""
# enumerate - нумерует список
"""
my_string = [1y2f34g56wery7890hh]
print(list(enumerate(my_string)))
"""
# zip - объединяет элементы списков по доступным значениям
# zip_longest - для вывода по максимальному количетсву элементов используется
"""
numbers = '1234567890'
letters = 'asdfghjk'
list_1 = list(numbers)
list_2 = list(letters)
print(list_1)
print(list_2)
new_list = list(zip(list_1, list_2))
print(new_list)
"""
# lambda
"""
numbers = '1234567890'
letters = 'asdfghjk'
list_1 = list(numbers)
list_2 = list(letters)
print(list_1)
print(list_2)
new_list = list(filter(lambda x: x.isdigit(), list_1))
print(new_list)
"""

# transformation = lambda x: x
# values = [2,3,5,7,11,13,17,19,23,29]
# transformed_values = list(map(transformation, values))
# print(values)


# from math import pi
# def find_farthest_orbit(list_of_orbits: list) -> tuple:
#     dict = {round(pi * orbit[0] / 2 * orbit[1] / 2, 2):
#             orbit for orbit in filter(lambda orbit: orbit[0] != orbit[1], list_of_orbits)}
#     return dict


# orbits = [(3, 2), (7, 4), (1, 22), (5, 5)]
# dict_p = find_farthest_orbit(orbits)
# print(max(dict_p), dict_p[max(dict_p)])


def same_by(characteristic, objects):
    my_set = set(map(characteristic, objects))
    return len(my_set) == 1

my_list = [2,4,6,8]
print(same_by(lambda objects: objects%2, my_list))