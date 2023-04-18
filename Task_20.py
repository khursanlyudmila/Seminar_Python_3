# Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.

# Напишите программу, которая вычисляет стоимость введенного пользователем слова. Будем считать, что на вход подается только одно слово

letters_list1 = str('AaEeIiOoUuLlNnSsTtRr')
list1 = list(letters_list1)
dict1 = dict.fromkeys(list1, 1)
letters_list2 = str('DdGg')
list2 = list(letters_list2)
dict2 = dict.fromkeys(list2, 2)
letters_list3 = str('BbCcMmPp')
list3 = list(letters_list3)
dict3 = dict.fromkeys(list3, 3)
letters_list4 = str('FfHhVvWwYy')
list4 = list(letters_list4)
dict4 = dict.fromkeys(list4, 4)
dict7 = {'K':5, 'k': 5}
letters_list5 = str('JjXx')
list5 = list(letters_list5)
dict5 = dict.fromkeys(list5, 8)
letters_list6 = str('QqZz')
list6 = list(letters_list6)
dict6 = dict.fromkeys(list6, 10)
my_dict = dict(list(dict1.items()) + list(dict2.items()) + list(dict3.items()) + list(dict4.items()) + list(dict5.items()) + list(dict6.items()) + list(dict7.items()))
user_word = str(input("Введите слово или последовательность букв на латинском языке: "))
user_world_list = list(user_word)
print(user_world_list)
answer_value = 0
for letter in user_world_list:
    if letter in my_dict:
        #for key in dict:    
        answer_value += my_dict[letter]
print(f"Стоимость введенного слова или последовательности букв равна - {answer_value}")