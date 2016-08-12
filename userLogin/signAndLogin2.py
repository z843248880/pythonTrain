#coding:utf-8
import sys
from random import Random

list_abc = {'one':'','two':'','three':''}   


def random_str(randomlength=8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str+=chars[random.randint(0, length)]
    return str


def sign_code_judge():
    count = 1
    while True:
        if count <3:
            #ran_num = random.randint(1,7)
            ran_str = random_str(4)
            print(ran_str)
            user_key_input = input('enter the code and continue to sign:')
            if user_key_input == ran_str:
                break
            else:
                print('you input a wrong code ,input again:')
        else:
            print('input code max times.bye')
            sys.exit()

      
def sign(username,password):
    f = open("user_two.txt",'a+')
    f.write(username)
    f.write(':')
    f.write(password)
    f.write('\n')
    f.close()
               
            
    
def login(username,password):
    f_black = open('black_two')
    for i in f_black.readlines():
        i = i.strip('\n')
        if i == username:        
            print ("your username is black")
            sys.exit()
            
    
    f_user = open('user_two.txt')
    f_user_read = f_user.readlines()
    for data in f_user_read:
        userName = data.split(':')[0]
        passWord = data.strip('\n').split(':')[1]
        if username == userName and password == passWord:
            print (username ,',welcome') 
            sys.exit()
while True:    
    user_choice = input('sign or login:')
    
    if user_choice == 'sign':
        sign_code_judge()
        username = input("please enter your username:")
        password = input("please enter your password:")
        sign(username, password)
        print('you had sign done.')
        break
    elif user_choice == 'login':
         
        count = 1
        while True:
            for key in list_abc:
                if count <= 3:               
                    username = input("please enter your username:")
                    password = input("please enter your password:")                    
                    login(username, password)
                    count += 1
                else:
                    break
                list_abc[key] = username
            print(list_abc)
            if list_abc['one'] == list_abc['two'] == list_abc['three']:
                f_black = open('black_two','a+')
                f_black.write(username)
                f_black.write('\n')
                f_black.close()
                print('max times,your username joined to black_list,try to contact administrator.')
                break
            else:
                print('please think your username&password ,then come back.')
                break
    
        break
    else:
        print('please choice sign or login,not other.')
    
    
    




