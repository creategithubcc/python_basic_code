str='abc cde f abc'
str1=str.replace('abc','qqq')
print('str=',str)
print('str=',str1)
str1=str.replace('abc','qqq',1)#替换一次
print('str=',str1)

#字符串分隔
result=str.split('a')#把a切割掉了，什么都不写就是空格
print(result)
result=str.rsplit('a',1)#切割一次而且从后往前
print(result)

str2='_'.join('aaaaaaa')#把—加入到字符串之间
print('str=',str2)
str2='_'.join('str')#把—加入到字符串之间
print('str=',str2)



