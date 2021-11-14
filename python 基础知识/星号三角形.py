'''while 1:
    n = eval(input('请输入数字：'))
    i = 0
    while i < n:
        j = 0
        while j < n:
            print('*', end=' ')
            j += 1
        print()
        i += 1
while 1:
    n = eval(input('请输入数字：'))
    i = 0
    while i<n:
        j=0
        while j<i+1:
            print('*',end=' ')
            j+=1
        print()
        i+=1'''
while 1:
    n = eval(input('请输入数字：'))
    for i in range(n):
        for j in range(i + 1):
            print('*', end=' ')
            j += 1
        print()
        i += 1

