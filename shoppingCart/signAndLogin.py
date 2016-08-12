#coding:utf-8

import sys
import random


dict_abc = {}   
sign_result = ''  

from random import Random
def random_str(randomlength=8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str+=chars[random.randint(0, length)]
    return str


def sign_code_judge(username):
    count = 1
    while True:
        if count < 3:
            #ran_num = random.randint(1,7)
            ran_str = random_str(4)
            print(ran_str)
            user_key_input = input('请输入验证码以继续:')
            if user_key_input == ran_str:
                break
            else:
                print('验证码错误，请重新输入:')
        else:
            print('验证码输入次数已满，再见。')
            sys.exit()
    f_user = open('user_two.txt')
    f_user_read = f_user.readlines()
    for data in f_user_read:
        if data.strip() == '':
            continue
        else:
            userName = data.split(':')[0]
            if username == userName:
                print (username ,',已经存在，请输入其他。') 
                return 'username is exist'
    

      
def sign(username,password):
    if sign_code_judge(username) == 'username is exist':
        return 'Sign False'  
    else:
        f = open("user_two.txt",'a+')
        f.write(username)
        f.write(':')
        f.write(password)
        f.write('\n')
        f.close()
        return 'Sign True'
        
    
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
        if user_choice == 'sign': 
            if sign(username,password) == 'Sign True':
                print('you had sign done.')
                return 'Sign OK'
                break
            else:
                print('not sign')
                break        
        elif user_choice == 'login':
            if traverse_username(username) != 'Traverse OK':
                return 'Traverse FALSE'
            if login(username, password) == 'OK':
                return 'login OK'
            else:
                break
        else:
            print('%s or %s' % (username,password))
            break 




