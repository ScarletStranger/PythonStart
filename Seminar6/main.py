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

import time 

n = int(input('Введите число от 1 до 10000 '))

# Первый способ
# start = time.time()
# def sum_divisors(n):
#     divisors = []
#     for i in range(1, n):
#         if n % i == 0:
#             divisors.append(i)
#     return sum(divisors)

# result = []
# for n in range(1, 10000):
#     m = sum_divisors(n)
#     if sum_divisors(m) == n and n != m:
#         result.append((n, m))
# print(result)
# end = time.time() - start
# print(end)


# Второй способ
start = time.time()
def friendly_numbers(n):
    if n <= 0:
        return []
    friends = []
    for i in range(2, 10001):
        while n % i == 0 and n > 0:
            friends.append(i)
            n //= i
    return sorted(friends)[::-1]
end = time.time() - start
print(end)