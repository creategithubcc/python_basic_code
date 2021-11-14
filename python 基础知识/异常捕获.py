num=input('输入一个数字：')
try:
    a=int(num)
    ans=100/a
    print(f'答案是：{ans}')
except ZeroDivisionError:
    print('输入有误，再次输入')
except ValueError:
    print('你输入错了')