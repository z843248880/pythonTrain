import re
from shoppingCart.showProduct import showProduct
from shoppingCart.saveProduct import saveProduct
from shoppingCart.clearProduct import clearProduct
from shoppingCart.buyProduct import buyProduct
from shoppingCart.printProduct import printProduct
from shoppingCart.showOtherChoice import showOtherChoice
from shoppingCart.showUserBalance import showUserBalance
from shoppingCart.showUserHistoryProduct import showHistoryProduct
from shoppingCart.delFromCart import delFromCart



def askUserBuy(username,user_balance):
    pList = []
    pDict = {}
    f = open('productList','r')
    fr = f.readlines()
    count_list = 1
    for i in fr:
        i = i.strip()
        pDict[count_list] = re.split(r'[\. ]', i)
        pList.append(i)
        count_list += 1
    pListIndexLen = len(pList) + 1
    #print(pListIndexLen)
    #print(pList)
    #print(pDict)
    #count = 1
    while True:
        #print('which product do your choice(number,please):')
        userChoice = input('which product do your choice(number1-%s,please):' % len(pList))
        if userChoice == 'l':
            showProduct()
            showOtherChoice()
        elif userChoice == 'c':
            clearProduct()
        elif userChoice == 'p':
            if printProduct(username) == 'Cart Empty':
                print('购物车是空的。')
                continue
            else:
                while True:
                    user_delcart_input = input('输入序号删除购物车物品，按q退出购物车,按p打印购物车商品：')
                    if user_delcart_input.isdigit():
                        delFromCart(username,int(user_delcart_input))
                    elif user_delcart_input == 'q':
                        break
                    elif user_delcart_input == 'p':
                        printProduct(username)
                    else:
                        continue
        elif userChoice == 'sb':
            showUserBalance(username)
        elif userChoice == 'sh':
            showHistoryProduct(username)
        elif userChoice == 'b':
            buyProduct(username,user_balance)
        elif userChoice == 'q':
            clearProduct()
            print('the shopping cart is cleared.bye,best wishes to you.')
            break
        elif userChoice.isdigit():
            listIndex = int(userChoice)
            #print(listIndex)
            for indexNum in range(pListIndexLen):
                #print(indexNum)
                if listIndex == indexNum:
                    productName = pDict[listIndex][1]
                    productPrice = int(pDict[listIndex][2].strip('$'))
                    print('%s 的价格是   %s,它将会加入到购物车中' % (productName,productPrice))
                    saveProduct(productName,productPrice)
        else:
            continue
            
            
    
