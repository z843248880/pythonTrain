from shoppingCart.clearProduct import clearProduct
from shoppingCart.showUserHistoryProduct import showUserHistoryProduct





def buyProduct(username,user_balance):
    print('您所选择的商品是:')
    print()
    f_cart = open('cartProduct','r')
    f_cart_read = f_cart.readlines()
    f_cart.close()
    for data in f_cart_read:
        #data = data.split(':')[0]
        print(data,end='')
    
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
    
    user_balance = user_balance - new_balance
    if user_balance < 0:
        print('您的余额不足，请充值或者减少商品，购买这些商品需充值：%d' % abs(user_balance))
        return 'balance not enough'
    
    balance_filename = 'balance_'+ username
    f_balance = open(balance_filename,'w')
    f_balance.write('%s' % user_balance)
    f_balance.close()
    print('您的余额是：%s' % user_balance)
    showUserHistoryProduct(username)
    clearProduct()
