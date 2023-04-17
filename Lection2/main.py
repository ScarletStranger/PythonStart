# Примеры создания списков
# list_1 = []
# list_1 = list{}
# list_1 = [1,2,4,67,44]
# list_1.append(k) - добавляет в список значение k
# print(*list_1) - вывод списка без скобок

# Удаление элементов списка
# Функци pop удаляет элемент по его значению
# list_1 = [12, 7, -1, 21, 0]
# print(list_1.pop()) # 0
# print(list_1) # [12, 7, -1, 21]
# print(list_1.pop()) # 21
# print(list_1) # [12, 7, -1]
# print(list_1.pop()) # -1
# print(list_1) # [12, 7]
# Также может удалить конкретный элемент по индексу
# list_1 = [12, 7, -1, 21, 0]
# print(list_1.pop(0)) # 12
# print(list_1) # [7, -1, 21, 0]

# Добавление элемента в список, где i - позиция, а v - значение
# list_1 = [12, 7, -1, 21, 0]
# print(list1.insert(i, v))
# print(list1) # [12, 7, 11, -1, 21, 0]

# Срезы
# list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_1[0]) # 1
# print(list_1[1]) # 2
# print(list_1[len(list_1)-1]) # 10
# print(list_1[-5]) # 6
# print(list_1[:]) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_1[:2]) # [1, 2]
# print(list_1[len(list_1)-2:]) #[9, 10]
# print(list_1[2:9]) # [3, 4, 5, 6, 7, 8, 9]
# print(list_1[6:-18]) # []
# print(list_1[0:len(list_1):6]) # [1, 7]
# print(list_1[::6]) # [1, 7]

# Кортеж - неизменяемый список, работает быстрее списка
# t=() или t=(1,4,5,) - пустой кортеж
# v = [1,8,9]
# v = tuple(v) - tuple преобразует список в кортеж
# a,b,c = v
# print(a,b,c) выведет 1 8 9 как отдельные переменные

# Словари = неупорядоченные коллекции произвольны объектов с достпуом по ключю
# В словаре для определения элементы используется значение ключа (строка, число)

# Пустой словарь
# dictionary = {}
# dictionary = dict{}

# dictionary ={'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
# Для вывода ключ указывается в квадратных скобках
# print(dictionary) выведет {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
# print(dictionary['left']) # ←

# типы ключей могут отличаться
# print(dictionary['up']) # ↑
# типы ключей могут отличаться
# dictionary['left'] = '⇐'
# print(dictionary['left']) # ⇐
# print(dictionary['type']) # KeyError: 'type'

# Удаление ключа
# del dictionary['left'] # удаление элемента
# for item in dictionary: # for (k,v) in dictionary.items():
# print('{}: {}'.format(item, dictionary[item]))
# up: ↑
# down: ↓
# right: →

# print(dictionary.items()) выводит ключ и его значение в виде кортежа

# Множества
# colors = {'red', 'green', 'blue'}
# print(colors) # {'red', 'green', 'blue'}
# colors.add('red')
# print(colors) # {'red', 'green', 'blue'}
# colors.add('gray')
# print(colors) # {'red','gray', 'green', 'blue',}
# colors.remove('red')
# print(colors) # {'green', 'blue','gray'}
# colors.remove('red') # KeyError: 'red'
# colors.discard('red') # ok
# print(colors) # {'green', 'blue','gray'}
# colors.clear() # { }
# print(colors) # set()

# Операции со множествами
# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy() # c = {1, 2, 3, 5, 8}
# u = a.union(b) # u = {1, 2, 3, 5, 8, 13,21}
# i = a.intersection(b) # i = {8, 2, 5}
# dl = a.difference(b) # dl = {1, 3}
# dr = b.difference(a) # dr = {13, 21}
# q=a.union(b).difference(a.intersection(b)) # {1, 21, 3, 13}

# Замороженное множество используется тогда, когда изначанльео множество не должно изменяться
# a = {1,8,4}
# b = frozenset(a)