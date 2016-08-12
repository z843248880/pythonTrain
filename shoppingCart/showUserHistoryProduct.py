import time

#current_time = '-------' + time.asctime() + '-------'

def showUserHistoryProduct(username):
    userHistoryProduct = 'history_product_' + username
    f_open_cart = open('cartProduct','r')
    f_cart_read = f_open_cart.read().strip()
    f_open_cart.close()
    
    f_open_product = open(userHistoryProduct,'a+')  
    f_open_product.write('-------%s-------' % time.asctime())
    f_open_product.write('\n')
    f_open_product.write(f_cart_read)
    f_open_product.write('\n')
    f_open_product.close()

def showHistoryProduct(username):
    userHistoryProduct = 'history_product_' + username
    f_open_product = open(userHistoryProduct,'r')
    f_read_product = f_open_product.readlines()
    for data in f_read_product:
        print(data,end='')



