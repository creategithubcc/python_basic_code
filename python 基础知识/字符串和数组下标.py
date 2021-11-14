name='hello'
print(type(name),name)

name="hello"
print(type(name),name)

name="'hello'"
print(type(name),name)

name='"hello"'
print(type(name),name)

str='hello'
print(str[0])
print(str[1])
print(str[-1])
print(str[-4])
print(str[-5])
print(len(str))
print('/////////')
print(str[len(str)-1])
str2=str[0:5:2]# 0<=str<5,间隔为2的字符串
print(str2)
str2=str[1:]# end部分不写取到最后
print(str2)
str2=str[:3]# sta部分不写从开头开始，间隔不写默认为1
print(str2)
str2=str[-4:-1]# el1
print(str2)
str2=str[3:1:-1]# l1
print(str2)

