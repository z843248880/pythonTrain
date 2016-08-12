

def delFromCart(username,user_delcart_input):
    list_del_index = int(user_delcart_input) - 1
    balance_file = 'balance_' + username 
    list_del = []
    f_cart = open('cartProduct','r')
    f_cart_read = f_cart.readlines()
    for data in f_cart_read:
        data = data.strip()
        list_del.append(data)
    '''
    f_open_balance = open(balance_file,'r')
    balance_value = f_open_balance.readline()
    f_open_balance.close()
    new_balance_value = int(balance_value) + int(list_del[list_del_index].split(':')[1])
    f_write = open(balance_file,'w')
    f_write.write(str(new_balance_value))
    f_write.close()
    #print(type(int(list_del[list_del_index].split(':')[1])))
   # print(list_del[list_del_index])
   '''
    if list_del_index > len(list_del) - 1:
        print('您输入的序号过大。')
    else:
        list_del.pop(list_del_index)
    f_cart = open('cartProduct','w')
    for dataw in list_del:
        f_cart.write(dataw)
        f_cart.write('\n')
    f_cart.close()

