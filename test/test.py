
import re
pList = []
pDict = {}
f = open('productList','r')
fr = f.readlines()
count = 1
for i in fr:
    i = i.strip()
    #print(re.split(r'[\. ]', i))
    pDict[count] = re.split(r'[\. ]', i)
    count += 1
    #pList.append(i)
    
print(pDict)
    
#print(pList)
#print(type(len(pList)))













'''
def test():
    username = input('username:')
    if username == 'zhang':
        return username
    else:
        return False
    

if test():
    print(test())
'''