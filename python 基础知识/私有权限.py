class people:
    def __init__(self):
        self.__a=0
    def money(self):
        return self.__a
    def setmoney(self,b):
        self.__a+=b

rl=people()
rl.__a=1000#重新添加了一个公有属性
print(rl.__a)

print(rl.money())
rl.setmoney(2000)
print(rl.money())
rl.setmoney(-500)
print(rl.money())









