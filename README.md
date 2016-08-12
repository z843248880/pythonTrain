# pythonTrain
train python with long.

## This program is a shopping cart.

- 1.first you download the shopping cart package
- 2.put the package to your IDE
- 3.run the main.py to test the program.

> this is a yinyong
> shide



######these are code
`if count <= 3:
            user_choice = input('sign or login or admin:')
            if re.match(r'(sign|login|admin)', user_choice) is None:
                print('请输入sign注册或者输入login登录。')
                continue
            if user_choice == 'admin':
                print('现在您已经进入管理模式。')
                adminProPri()
            print('现在进入用户模式。')
            username = input('username:')
            if username == '':
                print('%s 不能为空,请重新输入。' % username)
                continue
            password = input('password:')
            if password == '':
                print('%s 不能为空,请重新输入。' % password)
                continue
           
            dict_abc[count] = username
            if user_choice == 'sign':
                if login_cart(user_choice,username,password) == 'Sign OK':
                    print('注册成功，建议您选择login登录系统，祝您使用愉快。')
                else:
                    continue
            else:
                if login_cart(user_choice,username,password) == 'login OK':
                    break
                elif login_cart(user_choice,username,password) == 'Traverse FALSE':
                    print('%s ，没有这个用户，请选择sign注册。' % username)
                    continue
                else:
                    count += 1
                    print('%s or %s is invalid.' % (username,password))
                continue
            
        #print(dict_abc)
        elif dict_abc.get(int(1)) == dict_abc.get(int(2)) == dict_abc.get(int(3)) :
            f_black = open('black_two','a+')
            f_black.write(dict_abc.get(int(1)))
            f_black.write('\n')
            f_black.close()
            print('max times,your username joined to black_list,try to contact administrator.')
            sys.exit()
        else:
            print('please think your username&password ,then come back.')
            sys.exit()
        
      
    balance_filename = 'C:/Users/Administrator/workspace0725/day02/shoppingCart/balance_'+username
    if os.path.isfile(balance_filename) and os.path.getsize(balance_filename) != 0:
        f_user_balance = open(balance_filename,'r')
        user_balance = int(f_user_balance.readline().strip('$')) 
    else:
        while True:
            user_input_balance = input('系统显示当前没有您的余额记录，烦请填写（建议值：50-100000）:')
            if user_input_balance.isdigit():
                f_user_balance_w = open(balance_filename,'w')
                f_user_balance_w.write(user_input_balance)
                f_user_balance_w.close()
                #f_user_balance_r = open(balance_filename,'r')
                #user_balance_str = f_user_balance_r.readline()
                #f_user_balance_r.close()
                #user_balance = int(user_balance_str)
                break
            else:
                print('请输入合法数额（建议值：50-100000），谢谢。')
`
