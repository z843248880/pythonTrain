

dict_cart = {}
def saveProduct(productName,productPrice):
    dict_cart[productName] = productPrice
    f_cart = open('cartProduct','a+')
    f_cart.write(productName)
    f_cart.write(':')
    f_cart.write(str(productPrice))
    f_cart.write('\n')
    f_cart.close()
    
 