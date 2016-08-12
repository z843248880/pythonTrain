#coding:utf-8




test = ['a', 'b', 'c']
for k,v in enumerate(test):
    k = int(k) + 1
    print(k,v)













'''
class Province:
    country = "中国"
      
    def __init__(self, name):
        self.name = name
      
    @classmethod
    def show(cls):  # 类方法，由类调用，最少要有一个参数cls，调用的时候这个参数不用传值，自动将类名赋值给cls
        print(cls)
      
# 调用方法
Province.show()

'''










'''

print(divmod(15, 2))
'''




'''
res = map(lambda x:x**2,[1,2,3,4,5])
for i in res:
    print(i)
'''











'''
def cal(n):
    print(n)
    if int(n/2) == 0:
        return n
    return cal(int(n/2))

#cal(10)

print(cal(10))

'''











'''
b = '       Dsda    s$$$dsa      '
a = '     dfsd     '
print(a.strip())
print(b.replace('Dsda', 'anqing'))
print(b.rfind('dsa'))
print(b.rindex('Dsda'))

'''
