# list_1 = [x for x in range(1, 20)]
# print(list_1)

# list_1 = list(map(lambda x: x+10, list_1))
# print(list_1)

# .split - преобразует строку в список

# data = '15 987 61 979 5'
# print(data)
# data = list(map(int, data.split()))
# print(data)

data = [15, 45, 6, 7645, 564]
res = list(filter(lambda x: x % 10 == 5, data))
print(res)