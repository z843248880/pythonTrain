
import linecache

#count = linecache.getline('product_list', 2)
#print(count)
'''
s = 'pear:fdafdf'
s = s.replace('pear', 'watermelon')
print(s)
'''
product_name = '555'

f = open('product_list','r')
f_read = f.read()


f.close()
pos = f_read.find(product_name)
product_name_len = len(product_name)


if pos != -1:
    f_read = f_read[:pos] + '666' + f_read[pos+product_name_len:]
    f_write = open('product_list','w')
    f_write.write(f_read)
    f.close()
    print('replace.')

