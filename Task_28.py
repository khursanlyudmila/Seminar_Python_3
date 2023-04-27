# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# *Пример:*
# 2 2 Ответ 4
    
def sum_numbers(a, b):
    if b == 0:
        return a
    return sum_numbers(a+1, b-1)

a = int(input("Введите 1 число: "))
b = int(input("Введите 2 число: "))
print(f"Сумма чисел {a} и {b} = {sum_numbers(a, b)}")