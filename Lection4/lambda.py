# lambda-функция
# Пример
"""
calc(lambda x, y: x+y, 4, 5)
lambda x, y: - задаёт аргументы
x+y - действия с аргументами
4, 5 - значение аргументов
"""
"""
data =[1,2,3,5,8,15,23,38]
res = list()
for i in data:
    if i%2==0:
        res.append((i, i++2))
print(res)
"""

data =[1,2,3,5,8,15,23,38]
res = map(int, data)
res = filter(lambda x: x%2==0, res)
res = list(map(lambda x: (x, x**2), res))
print(res)