dict={'name':'cc'}
dict['age']=18#添加
print(dict)
dict['age']='十八'#修改
print(dict)
del dict['name']#删除
print(dict)
ans=dict.pop('age')
print(dict)
print(ans)
dict={'name':'cc','age':18}
print(dict)
dict.clear()
print(dict)
dict={'name':'cc','age':18}
result=dict.keys()
print(result,type(result))
for i in result:
    print(i)
print('*'*30)
for j,k in dict.items():
    print(j,k)
















