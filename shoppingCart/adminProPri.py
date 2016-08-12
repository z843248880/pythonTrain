
import sys

from shoppingCart.addProduct import addProduct
from shoppingCart.deleteProduct import deleteProduct
from shoppingCart.changePrice import changePrice
from shoppingCart.changeProductName import changeProductName
from shoppingCart.searchProduct import searchProduct

def adminProPri():
    while True:
        user_admin_choice = input('''
        输入a添加商品，
        输入d删除商品，
        输入ce改商品价格，
        输入ct改商品名称，
        输入s查看商品列表,
        输入q退出程序
   :''')
        if user_admin_choice == 'a':
            addProduct()
        elif user_admin_choice == 'd':
            deleteProduct()
        elif user_admin_choice == 'ce':
            changePrice()
        elif user_admin_choice == 'ct':
            changeProductName()
        elif user_admin_choice == 's':
            searchProduct()
        elif user_admin_choice == 'q':
            sys.exit()
        else:
            print('请输入a/d/ce/ct/s/q.')