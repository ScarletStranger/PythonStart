# Задача 26: Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

"""
num = int(input('Введите число '))
powe = int(input('Введите степень '))

def Power(num,powe):
    if powe == 0:
        return 1
    return num*Power(num,powe-1)

print(Power(num,powe))
"""

# Задача 24: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

num_1, num_2 = int(input('Введите первое число ')), int(input('Введите второе степень '))

def Total(num_1, num_2):
    return Total(num_1-1, num_2+1) if num_1 != 0 else num_2

print(Total(num_1, num_2))