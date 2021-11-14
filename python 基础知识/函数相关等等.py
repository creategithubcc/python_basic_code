def fun():
    ans = 0
    for i in range(5):
        ans+=i
        print(ans)
fun()

print('*'*20)

ans=0
def fun0(ans1):
    for i in range(5):
        ans1+=i
        print(ans1)
fun0(ans)

print('*'*20)

def add(a,b):
    c=a+b
    return c
'''a=eval(input('输入数字：'))
b=eval(input('输入数字：'))'''
a=1
b=2
ans=add(a,b)
print(f'答案是{ans}')

print('*'*20)

def add2(a,b):
    c=a+b
    d=a-b
    return [c,d]
a=2
b=2
ans=add2(a,b)
print(f'加法答案是{ans[0]},减法答案是{ans[1]}')







