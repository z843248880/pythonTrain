
def showProduct():
    product_list = []
    fProductList = open('productList','r')
    fRead = fProductList.readlines()
    print('PRODUCT LIST:')
    for data in fRead:
        print(data,end='')

    