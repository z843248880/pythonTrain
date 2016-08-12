
import re

def deleteProduct():
    f = open('productList','r')
    f_readlines = f.readlines()
    f.close()
    f1 = open('productList','w')
    f1.close()
    count = 0
    data_num = 1
    while True:
        proname = input('请输入要删除的商品名称，按q退出：')
        if proname == 'q':
            break
        
        else:
            for data in f_readlines:
                if data == '':
                    continue
                else:
                    data = data.strip()
                    print(data)
                    data_proName = re.split(r'[. ]', data)[1]
                    data_proPrice = re.split(r'[. ]', data)[2]
                    if data_proName == proname:
                        count = 1
                        continue
                    fw = open('productList','a')
                    fw.write('%d.' % data_num)
                    data_num += 1
                    fw.write(data_proName)
                    fw.write(' ')
                    fw.write(data_proPrice)
                    fw.write('\n')
                    fw.close()  
            if count == 0 :
                print('您输入的商品名称有误。') 
            else:
                print('删除成功。')
                break

