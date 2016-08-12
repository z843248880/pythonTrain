#product_name = 'watermelon'

def changeProductName():
    
    f = open('productList','r')
    f_read = f.read()
    f.close()
    while True:
        pro_old_name = input('请输入要删除商品名称：')
        pro_new_name = input('请输入修改后的商品名称：')
        pos = f_read.find(pro_old_name)
        product_name_len = len(pro_old_name)        
        if pos != -1:
            f_read = f_read[:pos] + pro_new_name + f_read[pos+product_name_len:]
            f_write = open('productList','w')
            f_write.write(f_read)
            f.close()
            print('商品名称已替换。')
            break
        else:
            print('您输入的商品名称不存在，请重新输入。')
        
        

