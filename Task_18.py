# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

#     5
#     1 2 3 4 5
#     6
#     -> 5

number_of_elements = int(input("Введите количество элементов массива: "))
import random
user_array = []
#user_array = [i for i in range(number_of_elements)]
for i in range(number_of_elements):
    user_array.append(random.randint(1,100))
print(user_array)
user_number = int(input("Введите число: "))
minimum = 10000000000
for i in user_array:
    if abs(i - user_number) < minimum:
        answer = i
        minimum = abs(i - user_number)
print(f"Самый близкий по величине элемент к заданному числу {user_number}  - {answer}")



# minimum = 1000
# setted_list = [2, 9, 6, 20, 15]
# value_chosen = 25

# for val in setted_list:
#     if abs(val - value_chosen) < minimum:
#         final_value = val
#         minimum = abs(val - value_chosen)
# print(final_value)