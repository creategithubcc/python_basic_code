class dog:
    def bark(self):
        print('汪汪汪')

    def eat(self):
        print('啃骨头')

class cat:
    def play(self):
        print('喵喵喵')
    def eat(self):
        print('吃猫粮')

class xtq(cat,dog):
    def eat(self):
        print('子类重写eat方法，调用子类自己的方法')
        #dog.eat(self)
        super(xtq, self).eat()
        super(cat, self).eat()
    pass

xtq1=xtq()
xtq1.bark()
xtq1.play()
xtq1.eat()
print('*'*20)













