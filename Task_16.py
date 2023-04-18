# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*

#     5
#     1 2 3 4 5
#     3
#     -> 1

number_of_elements = int(input("Введите количество элементов массива: "))
import random
user_array = []
for i in range(number_of_elements):
    user_array.append(random.randint(1,10))
print(user_array)
user_number = int(input("Введите искомое число из представленного массива: "))
quantity = 0
for i in user_array:
    if i == user_number:
        quantity += 1
print(f"Искомое число {user_number} встречается в массиве {quantity} раз")

