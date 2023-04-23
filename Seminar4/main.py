# Напишите программу, которая принимает на вход строку и отслеживает
# сколько раз каждый символ повторяется
# Количество повторов выводится через постфикс _n

string = list(input("Введите строку символов "))
count_dict = {}

for letters in string:
    count_dict[letters] = count_dict.get(letters, -1) + 1
print(f'{letters}' if count_dict.get(letters) == 0 else f'{letters}_{count_dict.get(letters)}', end =' ')