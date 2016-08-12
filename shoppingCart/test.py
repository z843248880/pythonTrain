import re
def addProduct():
    data_num = 0
    fr = open('productList','r')
    for data in fr.readlines():
        data = data.strip()
        data_num = int(re.split(r'[. ]', data)[0])
        
    fr.close()
    f_open = open('productList','a')
    data_num += 1
    while True:
        user_input = input('输入a添加商品，输入q退出程序：')
        if user_input == 'a':
            proname = input('请输入想要添加的商品名称：')
            proprice = input('输入该商品的价格（数字）：')
            while True:
                if proprice.isdigit():
                    fw = open('productList','a')
                    fw.write('%d.' % data_num)
                    data_num += 1
                    fw.write(proname)
                    fw.write(' ')
                    fw.write(proprice)
                    fw.write('\n')
                    fw.close()  
                    print('商品添加成功。')
                    break
                else:
                    print('价格必须是数字，请重新输入。')
                    break
        if user_input == 'q':
            break
        else:
            print('请输入a或者q。')
    






















'''
pro_old_name = input('请输入要删除商品名称：')
f = open('productList','r')
f_read = f.read()
f.close()
pos = f_read.find(pro_old_name)
print(pos)
'''













'''
def sign_code_judge(username):
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
     
def login_cart(user_choice,username,password):
    while True:    
        if user_choice == 'sign': 
            if sign(username,password) == 'Sign True':
                print('you had sign done.')
                return 'Sign OK'
                break  
            else:
                break
login_cart('sign', '666', '1623')   
'''