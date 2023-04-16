# Вывести индекс указанного числа Фибоначчи
# Если оно не является числом Фибоначчи, вывести -1
"""
fib_num = int(input('Введите число '))
fib1 = 0
fib2 = 1
index = 2

while fib2 < fib_num:
    fib1, fib2 = fib2, fib1+fib2
    index += 1
if (fib2 != fib_num):
    print('-1')
else:
    print(f'{fib_num} является {index} числом Фибоначчи')
"""

# Вывести количество дней, температуру которых подряд была выше 0
"""
import random

days = 30
count = 0
max_count = 0
today_temperature = 0

for i in range(days):
    today_temperature += random.randint(-3, 3)
    print(today_temperature, end=' ')
    if today_temperature > 0:
        count += 1
        if count > max_count:
            max_count = count
    else:
        count = 0
print(f'\n Самый долгий тёплый период - {max_count} дней подряд')
"""
# Указать количество арбузов и задать рандомом от 1000 до 30000 их вес
# Вывести наименьший и наибольший вес

import random

min_weight = 0
max_weight = 0
melons = int(input('Введите количество арбузов '))

for i in range(melons):
    melons_weight = random.randint(1000, 30000)
    if i == 0:
        min_weight=melons_weight
    if melons_weight>max_weight:
        max_weight=melons_weight
    elif melons_weight<min_weight:
        min_weight=melons_weight
print(f'\nЛегчайший арбуз весит {min_weight} грамм, а тяжелйший - {max_weight} грамм')
