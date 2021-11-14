class dog:
    class_name='狗狗'
    def __init__(self,name,age):
        self.name=name
        self.age=age
dog1=dog('大黄',2)
print(dog1.__dict__)
#print(dog.__dict__)
print(dog.class_name)
dog.class_name='GOULEI'
print(dog.class_name)

