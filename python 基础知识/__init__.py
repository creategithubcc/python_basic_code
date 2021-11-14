#构造函数__init__，在创建之后就会调用，1，给对象属性一个初始值（构造函数）
class dog(object):
    def __init__(self,name):
        print('我是__init__,我被调用了')
        #self.name='我是小狗'#对象.属性名=属性值
        self.name = name


#dog()
#dog1=dog()
#dog2=dog()
print('*'*20)
dog3=dog('大黄')
print(dog3.name)
dog4=dog('小白')
print(dog4.name)

















