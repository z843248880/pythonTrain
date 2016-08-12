import re
import sys
from shoppingCart.signAndLogin import random_str


def showUserBalance(username):
    fileName = 'balance_'+username
    fUserBalance = open(fileName,'r')
    fUserBalanceRead = fUserBalance.readline()
    fUserBalance.close()
    print('%s,your balance is %s.' % (username,fUserBalanceRead))
    #for data in fUserBalanceRead:
        #print(data,end='')
    charge_or_not = input('输入yes进行充值，输入q退出：')
    charge_re = re.match(r'(Yes|YES|yes|y)', charge_or_not)
    if charge_re:
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
                return 'Charge False'
            
        print('您的充值卡余额500元。')
        fUserBalanceOpen = open(fileName,'w')
        fUserBalanceRead = int(fUserBalanceRead) + 500
        fUserBalanceOpen.write(str(fUserBalanceRead))
        fUserBalanceOpen.close()
        print('now your balance is %d' % fUserBalanceRead)
        fUserBalanceOpen = open(fileName,'r')
        fUserBalanceRead = fUserBalanceOpen.readline()
        fUserBalanceOpen.close()
    return fUserBalanceRead
        
        
    
        
