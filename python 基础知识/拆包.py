#组包，将多个数据交给一个变量
a=1,2,3
print(a)

def func():
    return 4,5

b,c,d=a
print(b,c,d)

e,f=func()
print(e,f)
str=[10,20]
a,b=str
print(a,b)
dict={'name':'cc','age':18}
a,b=dict#key值
print(a,b)
print('*'*20)
a=10#a,b交换
b=20
a,b=b,a
print(f'a={a},b={b}')


















