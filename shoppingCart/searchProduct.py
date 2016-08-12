

def searchProduct():
    f = open('productList','r')
    for data in f.readlines():
        print(data,end='')

