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

limit = 10000
def Summa(limit):
    for i in range(1,limit-1):
        if 