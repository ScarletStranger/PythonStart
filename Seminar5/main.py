"""
import random
size = int(input('Введите количество оценок '))
maxi = int(input('Введите максимальную оценку '))
mini = int(input('Введите минимальную оценку '))
my_list = [random.randint(mini, maxi) for _ in range(size)]
print(my_list)
maxi = max(my_list)
mini = min(my_list)
my_list = [mini if i == maxi else i for i in my_list]
print(my_list)
"""
"""
num = int(input('Введите число '))

def is_prime(num) -> bool:
    if num in [1, 2]:
        return True
    elif num % 2 == 0:
        return False
    else:
        for i in range(3, num // 2 + 1, 2):
            if num % i == 0:
                return False
        return True

print(f"Число {num} " + ("простое"if is_prime(num) else "составное"))
"""

#Строка

string = input("Введите строку символов ")

def Reverse(string):
    if len(string)==1:
        return string
    else:
        return string[-1] + Reverse(string[:-1])

print(Reverse(string))
