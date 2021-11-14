print('hello worrld')#这是一个注释，另外绿色下划线代表你写的不是英文单词
'''这是一个多行注释       #比如worrld
也可以用双引号三个'''

"""比如像这样"""

name='num'#定义一个变量num，不需要int float的生申明
age=10
print(name)
print(age)
age=20
print('age变成了')
print(age)

#int类型
num=10
print(type(num)) # <class 'int'>
#str字符串
num='ooo'#双引号也可以
name='苍苍'
print(type(num))
'''一次性输出多个内容'''
print('okok',10101)
print(1+2+3+4,5+6+7+8)
print("我是%s" %name)
height=178.5
print('我的身高是：%.2f' %height)
print('我是%s,我的身高是：%.2f' %(name,height))#####!!!
print('百分比是%d%%' %50)
print(f"my name is {name},my height is {height}")#!!!!
'''去掉默认的换行'''
print('hello')
print('world')

print('hello',end=' ')
print('world')

print('hello',end='!*%/+#')
print('world')

print('good\nstudy')

#input()括号中不写内容，语法不会出错，但是不知道做什么
password=input('请输入密码：')
print('你输入的密码是：%s'%password)

ppp=input('请输入苹果价格：')
rrr=input('请输入香蕉价格：')
result=float(ppp)*float(rrr)#类型转换成float
print(f'苹果价格{ppp}元，香蕉价格{rrr}元，两者相乘{result}元')

pi=3.14
num=int(3.14)
print(type(pi))
print(type(num))
print(num)

#整数类型string字符串
str='10'
num1=int(str)
print(type(num1))
print(str)#字符串类型
print(num1)#整数类型
#eval()还原原来的数据类型，去掉字符串引号
num2=eval('100')
num3=eval('3.14')
print(type(num2))
print(type(num3))
num5=eval('num3')
print(num5,type(num5))