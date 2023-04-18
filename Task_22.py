# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.

user_number1 = int(input("Введите размер первого множества: "))
user_number2 = int(input("Введите размер второго множества: "))
import random
user_list1 = []
user_list2 = []
for i in range(user_number1):
    user_list1.append(random.randint(1, 20))
user_set1 = set(user_list1)
for j in range(user_number2):
    user_list2.append(random.randint(1, 20))
user_set2 = set(user_list2)
#a = [int(i) for i in input().split()]
print(user_set1)
print(user_set2)
user_intersection = user_set1.intersection(user_set2)
user_intersection_sort = sorted(user_intersection)
print(user_intersection_sort)