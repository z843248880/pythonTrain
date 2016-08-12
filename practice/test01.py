#coding:utf-8














'''
a = 'Dsdasd$sa'
b = 'Dsdasdsa'
c = '#$_ ds '
print(('_'.join(a))















'''
a = 'fdsEWREWfdsf'
b = '44#fda34'
c = 'fder$#'
d = ' '
e = '1232143'
f = '_4312'
print(a.isnumeric())
print(b.isnumeric())
print(c.isnumeric())
print(d.isnumeric())
print(e.isnumeric())
print(f.isnumeric())
'''











'''
people = {
          'name':['zhang','ci'],
          'age':[55,33]
          }

print(['my name is {},my age is {}'.format(*x) for x in zip(people['name'],people['age'])])
print(['my name is {},my age is {}'.format(*x) for x in zip(*map(people.get,['name','age']))])
'''


'''
print(people)

print('my name is {name[0]},my age is {age[0]}'.format_map(people))
print('my name is {name[0]},my age is {age[1]}'.format_map(people))
print('my name is {name[1]},my age is {age[0]}'.format_map(people))
print('my name is {name[1]},my age is {age[1]}'.format_map(people))
'''


















'''
a = 'fdjai\tjoia'
print(a.capitalize())
print(a.center(40,'-'))
print(a.expandtabs())
print("----->{%s}" % a)
print(a.title())
print(a.translate(1))





print('--------------------------------------')
b = 'abc.txt'
print(b.endswith('.txt'))


c= '张善慈'
print(c)
print(c.encode())
print(c.encode().decode())

'''













'''
import sys
print(sys.argv)
'''





'''
f_open = open('productList','a')
while True:
    user_input = input('输入a添加商品，输入q退出程序：')
    if user_input == 'a':
        proname = input('请输入想要添加的商品名称：')
        proprice = input('输入该商品的价格（数字）：')
        while True:
            if proprice.isdigit():
                f_open.write(proname)
                f_open.write(':')
                f_open.write(proprice)
                f_open.write('\n')
                f_open.close()
                print('商品添加成功。')
                break
            else:
                print('价格必须是数字，请重新输入。')
                break
    if user_input == 'q':
        break
    else:
        print('请输入a或者q。')
'''







'''
f = open('test','r')
f_readlines = f.readlines()
f.close()
f1 = open('test','w')
f1.close()
count = 0
for data in f_readlines:
    if data == '':
        continue
    else:
        data = data.strip()
        data_proName = data.split(':')[0]
        data_proPrice = data.split(':')[1]
        if data_proName == proname:
            count = 1
            continue
        fw = open('test','a')
        fw.write(data_proName)
        fw.write(':')
        fw.write(data_proPrice)
        fw.write('\n')
        fw.close()  
if count == 0 :
    print('您输入的商品名称有误。') 
            #break     
'''           




























'''
num = 4 * 4 * 4 * 4 *4

print(num)








class Bird(object):
    def __init__(self):
        self.hungry = True
    def eat(self):
        if self.hungry:
            print('aaaa')
            self.hungry = False
        else:
            print('nonono')
            

class SonBird(Bird):
    def __init__(self):
        super(SonBird,self).__init__()
        self.Name = 'zhang'
    def sing(self):
        print(self.Name)

sb = SonBird()
sb.sing()

sb.eat()
sb.eat()


'''







'''
class A:
    def hello(self):
        print('hello A')
        
class B(A):
    def hello(self):
        print('hello B')

a = A()
b = B()

a.hello()
b.hello()
'''
'''