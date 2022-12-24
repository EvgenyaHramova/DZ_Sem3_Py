# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random

n = int(input("Введите количество элементов списка: "))
rand_list = []
for i in range(n):  # генерируем в цикле случайные числа в заданном количестве и диапазоне
    rand_list.append(random.randint(1, 11))
print('Сгенерирован следующий список: ', rand_list)

if (len(rand_list)) % 2 == 0:
    lenght2 = int((len(rand_list)) / 2)
else:
    lenght2 = int((len(rand_list) / 2) + 1)

list2 = []

for j in range(lenght2):
    n = n - 1
    a = rand_list[j] * rand_list[n]
    list2.append(a)
    
print('Произведение пар чисел первоначального списка равна', list2)
