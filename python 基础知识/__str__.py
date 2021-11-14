class dog(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        print('我是__str__，我被调用了')
        return f'小狗名字叫{self.name},年龄是{self.age}'

dog1=dog('大黄',2)
print(dog1)#没有定义__str__，默认输出对象引用地址
strdog=str(dog1)
print(strdog)#完全一样，没有定义的话











