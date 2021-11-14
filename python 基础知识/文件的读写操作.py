f=open('1.txt','r',encoding='utf-8')#以只读的方式打开当前目录文件
buf=f.read()
print(buf)

print('*'*20)

f=open('1.txt','w',encoding='utf-8')#打开当前目录文件
f.write('niconiconi\n')#写入
f.write('a na ta no ha to ni\n')
f.write('我是奥特曼,好耶')
f.close()#不加这句代码的话就不会保存我们刚刚的操作

print('*'*20)

f=open('2.txt','a',encoding='utf-8')#a代表打开方式或创建文件
f.close()

print('*'*20)

f=open('2.txt','r',encoding='utf-8')
buf=f.read(3)
print(buf)
print('*'*20)
buf=f.read(3)
print(buf)
f.close()

print('*'*20)
f=open('2.txt','r',encoding='utf-8')
buf=f.readline()#一次读取一行
print(buf)
f.close()











