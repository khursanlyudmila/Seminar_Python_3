# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент,
# разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

a1 = int(input("Введите первый элемент арифм.прогрессии: "))
diff = int(input("Введите разность арифм.прогрессии: "))
quant = int(input("Введите количество элементов арифм.прогрессии: "))
user_array = list(range(a1, a1 + quant*diff, diff))
print(user_array)