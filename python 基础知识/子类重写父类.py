class dog:
    def bark(self):
        print('汪汪汪')


class xtq(dog):
    def bark(self):#重载
        print('嗷嗷嗷')

    def see(self):
        print('看见主人了',end=' ')
        #dog.bark(self)#作为对象传递就不要self，但这是作为父类的传递
        #super(xtq, self).bark()#调用xtq的弗雷里面的bark
        super().bark()
        pass

xtq1=xtq()
xtq1.bark()
xtq1.see()
print('*'*20)
dog1=dog()
dog1.bark()














