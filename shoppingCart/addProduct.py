
import re
def addProduct():
    data_num = 0
    fr = open('productList','r')
    
    for data in fr.readlines():
        data = data.strip()
        data_num = int(re.split(r'[. ]', data)[0])
    fr.close()
    f_open = open('productList','a')
    data_num += 1
    while True:
        user_input = input('输入a添加商品，输入q退出程序：')
        if user_input == 'a':
            proname = input('请输入想要添加的商品名称：')
            proprice = input('输入该商品的价格（数字）：')
            while True:
                if proprice.isdigit():
                    fw = open('productList','a')
                    fw.write('%d.' % data_num)
                    data_num += 1
                    fw.write(proname)
                    fw.write(' ')
                    fw.write(proprice)
                    fw.write('\n')
                    fw.close()  
                    print('商品添加成功。')
                    break
                else:
                    print('价格必须是数字，请重新输入。')
                    break
        if user_input == 'q':
            break
        else:
            print('请输入a或者q。')

