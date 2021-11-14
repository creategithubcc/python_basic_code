str=[]
print(str,type(str))
str1=list()
print(str1,type(str1))

str2=[1,3.14,True,'aaa']#字符串？数组 list类型数组
print(str2,type(str2))
num=(str2)
print(num)
print(str2[1])
print(str2[-1])
print(str2[1:3])
str2[0]=17
print(str2)
str2[-1]='hello'
print(str2)
print('*'*20)
str3=['a','b','c','d']
for i in str3:  #这一块不需要range（），range主要是为了体现遍历循环次数
    print(i)
print('*'*20)
i=0
while i < len(str3):
    print(str3[i])
    i+=1

str3.append('aa')#添加一个数据
print(str3)
str3.append(12)
print(str3)
str3.insert(0,'qqq')#在0添加入一个qqq
print(str3)
str3.extend('qqq')#在0添加入一个qqq,分别添加q,q,q
print(str3)
num1=str3.count('qqq')
num1=3.14 in str3#判断是否存在
print(num1)
str3.remove('qqq')#删除数据
print(str3)
str3.pop(2)#删除数据下标2
print(str3)
del str3[2]#删除数据下标2
print(str3)
str4=[1,5,6,9,2,7]
str4.sort()
print(f'aaaaaaaaaaa:{str4}')#括号内部不写默认从小到大
str4.sort(reverse=True)#排序操作，从大到小,Flash就是从小到大，reverse是逆转的意思
print(str4)
str5=sorted(str4,reverse=True)#排序操作，但是不会在原列表中显示，会生成一个新的列表
print(str5)
str6=['p','q','a','s','d','r','g','i']
str7=str6[::-1]
print(str6)
print(str7)
str6.reverse()#直接在原来数组逆转
print(str6)

