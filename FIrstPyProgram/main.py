file = open('names.txt', 'r', encoding='utf-8')

list_1 = list()
result_data = list()
for line in file.readlines():
    print(line.split('\n')[0].split(';'))
    result_data.append(tuple(line.split('\n')[0].split(';')))

file.close()

print(result_data)