"""
#За сколько дней машина проедет b киллометров, если за день она проезжает a киллометров

import math
a = int(input("Input a distance which car rides in one day "))
b = int(input("Input a distance which car has to ride "))
print(f"A car has to drive for {math.ceil(b/a)} days to ride {b} kilometres")
print(f"A car has to drive for {(b+a)//a} days to ride {b} kilometres")
# math.ceil всегда округляет в большую сторону
"""

"""
#У каждого из трёх классов указать количество учеников.
#У каждого класса свой кабинет.
#За каждой партой может сидеть два ученика.
#Вывести наименьшее число парт для всех учеников.

a = int(input("Input a number of students in the first class "))
b = int(input("Input a number of students in the second class "))
c = int(input("Input a number of students in the third class "))
print(f"First class needs {(a+1)//2} desks for {a} students")
print(f"Second class needs {(b+1)//2} desks for {b} students")
print(f"Third class needs {(c+1)//2} desks for {c} students")
print(f"All classes need {((a+1)//2)+((b+1)//2)+((c+1)//2)} desks in total")
print(f"All classes need {(a+b+c)//2+((a+b+c)%2)} desks in total")
"""

"""
# Вагоны пронумерованы натуральными числами, начиная с 1
# Вагоны нумеруются в зависимоти от направления движения,т.е.
# Если от начала до конечной, то первый вагон будет первым
# Если от конечной до начала, то последний вагон будет первым
# Витя сел в i вагон от головы поезда, но номер вагона был j
# Определить количество вагонов в электричке или указать почему это не возможно

i = int(input("В какой вагон с головы сел Витя? "))
j = int(input("Введите настоящий номер вагона, в который сел Витя "))
if(i==j):
    print("Нужно больше информации")
else:
    print(f"В поезде {i+j-1} вагонов")
"""

# Указать год и определить является ли он весокосным

year = int(input("Введите год "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} - високосный год")
else:
    print(f"{year} - високосный год")
