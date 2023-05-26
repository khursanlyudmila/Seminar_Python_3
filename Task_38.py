# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной
# записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных

def readfile(filename):
    data = [i.split() for i in open(filename, 'r', encoding='utf-8')]
    return data


def printinfo(data):
    for i in data:
        print(' '.join(i))

def get_new_number():
    number = input('Введите порядковый номер: ')
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    surname = input('Веедите отчество:')
    phone_number = input('Введите номер телефона: ')
    return number, last_name, first_name, surname, phone_number


def add_phone_number(data):
    info = ' '.join(get_new_number())
    with open('telephone_list.txt', 'a', encoding='utf-8') as file:
        file.write(f'{info}\n')
    print(f'В справочник добавлена следующая информация: {info}\n')

def find_info(data): # Поиск данных
    search = input('Введите данные для поиска: ')
    search_result = []
    for i in data:
        if search in i:
            search_result.append(i)
    if len(search_result) == 0:
        print('Данные не найдены!')
    else:
        for i in search_result:
            print(' '.join(i))
        #print(*search_result, sep='\n')

def change(data): # Изменение данных
    old_info = input('Введите данные, которые хотите заменить: ')
    new_info = input('Введите новые данные: ')
    with open('telephone_list.txt', 'r', encoding='utf-8') as file:
        old_file = file.read()
    new_file = old_file.replace(old_info, new_info)
    with open('telephone_list.txt', 'w', encoding='utf-8') as file:
        file.write(new_file)
    print("Данные успешно обновлены!")

# def change(data): # Изменение данных
#     old_info = input('Введите данные, которые хотите заменить: ')
#     new_info = input('Введите новые данные: ')
#     with open('telephone_list.txt', 'r', encoding='utf-8') as file:
#         old_file = file.readlines()
#         element = 0
#         for i in old_file:
#             if  old_info in i:
#                 Replacement = old_file.replace(old_info, new_info)
#                 old_file = Replacement
#             element +=1
#             # else:
#             #     print("Данные не найдены!")
#     file.truncate(0)
#     file.writelines(old_file)
#     file.close()
#     print("Данные успешно обновлены!")

def delete_person(data): # Удаление данных при условии, что вся строка файла совпадает с введенной строкой для удаления!
    delete_info = input('Введите данные для удаления: ')
    with open('telephone_list.txt', 'r', encoding='utf-8') as file:
        old_file = file.readlines()
    with open('telephone_list.txt', 'w', encoding='utf-8') as file:
        for line in old_file:
            if line.strip("\n") != delete_info:
                file.write(line)
    print("Данные успешно удалены!")

def finish(data):
    print('До следующей встречи!')
    exit()

def main():
    my_choice = -1
    data = readfile('telephone_list.txt')
    while my_choice != 0:
        print('Выберите одно из действий:')
        print('1 - вывод данных на экран')
        print('2 - добавление данных')
        print('3 - поиск данных')
        print('4 - изменение данных')
        print('5 - удаление данных')
        print('0 - выход из программы')
        my_choice = int(input())
        operations = {1: printinfo, 2: add_phone_number, 3: find_info, 4: change, 5: delete_person, 0: finish}
        operations[my_choice](data)

if __name__ == '__main__':
    main()