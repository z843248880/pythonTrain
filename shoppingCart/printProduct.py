

def printProduct(username):
    f_cart = open('cartProduct','r')
    f_cart_read = f_cart.readlines()
    count = 1
    for data in f_cart_read:
        if data == '':
            continue
        else:
            print(count,data,end='')
            count += 1
    if count == 1:
        return 'Cart Empty'
    
    list_price = []
    cart_read = open('cartProduct','r')
    cart_read_lines = cart_read.readlines()
    cart_read.close()
    for data in cart_read_lines:
        data_price = data.split(':')[1]
        list_price.append(data_price)
    new_balance = 0
    for price in list_price:
        new_balance = new_balance + int(price)
    print('购物车物品总额:%d' % new_balance)
    
    balance_file = 'balance_' + username
    with open(balance_file,'r') as f_read:
        print('您的可用余额是：%s' % f_read.readline()) 
