"""
import random
size_1, size_2 = int(input('Введите размер первого списка ')), int(input('Введите размер второго списка '))
my_list_1, my_list_2 = {random.randint(1, 50) for _ in range(size_1)}, {random.randint(1, 50) for _ in range(size_2)}
print(f"{my_list_1}{my_list_2}")
print(sorted(my_list_1.difference(my_list_2)))
"""

"""
import random
size = int(input('Введите размер списка '))
my_list = [random.randint(1, 50) for _ in range(size)]
print (my_list)
count = 0
for i in range (0, (len(my_list)-1)):
    if my_list[i-1]<my_list[i]>my_list[i+1]:
        count +=1
        print (count, my_list[i])
"""

"""
import random
size = int(input('Введите размер списка '))
my_list = [random.randint(1, 10) for _ in range(size)]
print (my_list)
print(sum([my_list.count(i)//2 for i in set(my_list)]))
"""

# Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n (включая 1, но исключая само n)
# равна числу m и наоборот.
# Например числа 220 и 284 - дружественные.
# Dыведите все пары дружественных чисел до k=10000

n = int(input('Введите число от 1 до 10000 '))

def Summa(n):
    summ = 0
    for k in range(1, n//2+1):
        if n % k == 0:
            summ += 1
    return summ

for i in range(1, 10000):
    j = Summa(i)
    if i < j <= n and i == Summa(j):
        print(i,j)
