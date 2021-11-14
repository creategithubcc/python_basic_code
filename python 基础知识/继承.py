class animal:
    def play(self):
        print('快乐玩耍中......')


class dog(animal):
    def bark(self):
        print('汪汪汪')


class xtq(dog):
    pass

xtq1=xtq()
xtq1.bark()
xtq1.play()

dog1=dog()
dog1.play()