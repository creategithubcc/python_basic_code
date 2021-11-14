class dog:
    def born(self):
        print('生了一只狗')
        self.__sleep()
    def __sleep(self):
        print('休息三十天')
dog1=dog()
dog1.born()
#dog1.__sleep()#变成私有化后无法调用
