from random import randint

def generate_fb(db_len = 1000):
    my_dic = {}
    alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЪъЭЮЯ'
    for item in range(db_len):
        name_len = randint(6, 10) #Длина фамилии    
        surname = ''    
        for i in range(name_len):
            surname += alphabet[randint(0, 32)]
        fullname = surname + ' ' + alphabet[randint(0, 32)]+ '.' + alphabet[randint(0, 32)]+ '.'
        if randint(0, 1): sex = 'мужчина'
        else: sex = 'женщина'
        birthday = str(randint(1, 28)) + '.' + str(randint(1, 12))+ '.' + str(randint(1950, 2022))
        phone_number = str(randint(1000000000, 9999999999))
        my_dic[item] = [fullname, sex, birthday, phone_number]
    return my_dic

def write_file(my_dic, filename = 'phonebook.csv'):
    with open(filename, 'a') as data:
        for man in my_dic:
            data.write(';'.join(my_dic[man]))
            data.write('\n')
    return print('Запись выполнена')

def read_file(filename = 'phonebook.csv'):
    with open(filename, 'r') as data:
        count = 0
        my_dic = {}
        for line in data:            
            my_dic[count] = line[:-2].split(';') #Срезом убираем символ перевода строки
            count +=1
    print('Чтение выполнено успешно')
    return my_dic

def find_name(my_dic, my_key):
    title = ['Fullname :', 'Sex:', 'Birthday :','Phone Number:']
    print()
    if my_key in my_dic: 
        for item in range(4):         
            print(title[item], my_dic[my_key][item])
    else: print('Такого чувака нет в нашей базе данных')
    # print(*list(zip(title, my_dic[my_key])))
    return

def print_db(my_dic):
    for key in my_dic: print(my_dic[key])