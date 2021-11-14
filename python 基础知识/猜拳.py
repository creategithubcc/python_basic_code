import random
user=eval(input('请输入1.拳头 2.剪刀 3.布 ：'))
computer=random.randint(1,3)#随机产生1-3的数字
if user==1:
    str='拳头'
elif user==2:
    str='剪刀'
else :
    str='布'
print(f'你出了{str}')
if computer==1:
    str='拳头'
elif computer==2:
    str='剪刀'
else :
    str='布'
print(f'电脑出了{str}')
if user==computer:
    print('平局')
elif (user==1 and computer==2)or(user==2 and computer==3)or(user==3 and computer==1):
    print('you win')
else:
    print('you lost')