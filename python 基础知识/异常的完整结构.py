num=input('输入一个数字：')
try:
    a=int(num)
    ans=100/a
    print(f'答案是：{ans}')
    f=open('155.txt','r')
except Exception as e:#打印所有异常信息
    print('输入有误，再次输入',e)
else:
    print('没有发生异常我会执行')
finally:
    print('不管有没有发生异常，我都会执行')

print('其他代码......')