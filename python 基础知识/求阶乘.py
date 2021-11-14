def fun(n):
    num=1
    for i in range(1,n+1):
        num=num*i
    print(num)

def fun2(n):
    if(n==1):
        return 1
    num=fun(n-1)*n
    return num

m=eval(input('请输入求积数：'))
fun(m)










