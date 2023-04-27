# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

numbers = int(input("Введите количество элементов массива: "))
import random
lst = []
for i in range(numbers):
    lst.append(random.randint(1,100))
print(lst)
minimum = int(input("Введите минимум диапазона: "))
maximum = int(input("Введите максимум диапазона: "))

# 1-ый вариант:
for i in range(len(lst)):
    if lst[i] >= minimum and lst[i] <= maximum:
           print(i, end=": ")
           print(lst[i])

# 2-ой вариант:
# print(*[i for i, j in enumerate(lst) if j >= minimum and j <= maximum])
