# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным
# и минимальным значением дробной части элементов.

# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19



list = []
n = int(input('Введите размер списка с клавиатуры: '))
print('Введите вещественные числа элементов списка: ')
for x in range(n):
    x = float(input())
    list.append(x)
print(list)

list1= []
for i in list:
    y = round((i - int(i)), 5)
    list1.append(y)
# print(list1)

maxx = list1[0]
for i in list1:
    if i > maxx:
        maxx = i
    else:
        minn = i
print(maxx - minn)