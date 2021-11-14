class dog:
    def __init__(self,name):
        self.age=0
        self.name=name

    def __str__(self):
        return f'年龄是：{self.age},名字是:{self.name},颜色是：{self.color}'


class xtq(dog):
    def __init__(self,name, color):
        super().__init__(name)
        self.color = color
    pass

xtq1=xtq('小黑','红色')

print(xtq1)
print('*'*20)















