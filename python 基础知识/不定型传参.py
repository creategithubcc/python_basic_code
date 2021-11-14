def fun(*args,**kwargs):#在形参前面加个*，变成不定长元组形参，可以接受所有位置实参
    print(args)#加个**，变成不定长字典形参，可以接收所有关键字实参，类型是字典
    print(kwargs)

fun(1, 2)
fun(args=2, kwaegs=1)

fun(1,2,3,4,5)
fun(a=1,b=2,c=3,d=4,e=5)
print('*'*20)
def fun1(*args,**kwargs):
    num=0
    for i in args:
        num+=i
    for i in kwargs.values():
        num+=i
    print(f'求和结果为{num}')
fun1(1,2,3,a=4,b=5,c=6)









