dict0={}
dict1=dict()
print(dict0,type(dict0))
print(dict1,type(dict1))
dict2={'name':'苍苍','age':18 ,'like':['学习','游戏','购物'],1:[2,5,8]}
print(dict2)
#字典当中没有下标概念,只能通过key去访问
print(dict2['name'])
print(dict2['like'])
print(dict2['like'][1])#列表可以用下标
print(dict2.get(1)[1])
print(dict2.get('sex','男'))
print(dict2.get('age',10))







