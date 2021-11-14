'''age=input('请输入年龄：')
#需要将字符串类型的age转换成int类型
age=int(age)'''

age=eval(input('输入年龄：'))
if age>=18:
    print('哥十八了，进去！')
elif age>=14 and age<18:# >=14且<18
    print('你还不满十八')
elif age>=10 or age<10:#或||运算
    print('你还不满十八2')
else:
    print('nono,不行啊')
print('if判断结束')

