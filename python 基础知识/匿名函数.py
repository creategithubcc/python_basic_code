def calc(a,b,fun):
    num=fun(a,b)
    return num
def add(a,b):
    return a+b
print(calc(10,20,add))
print(calc(10,20,lambda a,b:a*b**2))








