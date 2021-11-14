str='hello my python'
j=0
for i in str:
    j+=1
    if i=='p':#python里面if else不一定在一个嵌套里
        print(f'第{j}个字符包含p字符')
        break
else:
    print('不包含p字符')