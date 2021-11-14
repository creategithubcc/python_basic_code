class dog(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f'小狗名字叫{self.name},年龄是{self.age}'
    def __del__(self):
        print(f'我是__del__，我被调用了,{self.name}被销毁了')


dog1=dog('大黄',2)
print(dog1)
dog2=dog('小白',5)
print(dog2)
dog3=dog('小花',7)
#dog4=dog3
print('第1次删除之前')
del dog3
print('第1次删除之后')
print('第2次删除之前')
#del dog4
print('第2次删除之后')







