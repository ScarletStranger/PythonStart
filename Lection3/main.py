# Функция в питоне означается оператором def
# Пример
"""
def summ(n): или def summ(*args), где *args используется, когда количество аргументов неизвестно
    summa = 0
    for i in range(1, n+1):
        summa += i
    return summa
print(summ(5))
"""
# Фибоначчи через рекурсию
"""
def fib(n):
    if n in [1,2]:
        return 1
    return fib(n-1) + fib(n-2)
list_1 = []
for i in range(1, 10):
    list_1.append(fib(i))
print(list_1)
"""