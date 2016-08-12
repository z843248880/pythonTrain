import sys
import random

dict_abc = {}   
sign_result = ''     
def traverse_username(username):
    f_user = open('user_two.txt')
    f_user_read = f_user.readlines()
    for data in f_user_read:
        if data.strip() == '':
            continue
        else:
            userName = data.split(':')[0]
            if username == userName:
                return 'Traverse OK'
   
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
        if data.strip() == '':
            continue
        else:
            userName = data.split(':')[0]
            passWord = data.strip('\n').split(':')[1]
            if username == userName and password == passWord:
                print (username ,',welcome') 
                return 'OK'
     
def login_cart(user_choice,username,password):
    
    while True:    
        if user_choice == 'login':
            if traverse_username(username) != 'Traverse OK':
                print('diguishibai')
                return 'Traverse FALSE'
            if login(username, password) == 'OK':
                print('login OK')
                return 'login OK'
            else:
                print('mima cuowu')
                break
        else:
            print('%s or %s' % (username,password))
            break

login_cart('login', '123', '456')