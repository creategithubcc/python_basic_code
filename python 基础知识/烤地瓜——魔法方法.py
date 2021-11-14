class potato:
    def __init__(self):
        self.status='生的'
        self.totaltime=0
        self.name_list=[]
    def cook(self,time):
        self.totaltime+=time
        if(self.totaltime<3):
            self.status='生的'
        elif(self.totaltime<6):
            self.status='半生不熟'
        elif(self.totaltime<8):
            self.status='熟的'
        else:
            self.status='烤焦了'
    def __str__(self):

        if(self.name_list):
            return f'地瓜的状态：{self.status}     地瓜的烧烤时间：{self.totaltime}     调料有{self.name_list}'
        else:
            return f'地瓜的状态：{self.status}     地瓜的烧烤时间：{self.totaltime}     无调料'
    #def __del__(self):
    def add(self, name):
        self.name_list.append(name)



potato1=potato()
print(potato1)
potato1.add('辣椒酱')
potato1.cook(2)
print(potato1)
potato1.add('麻辣酱')
potato1.cook(3)
print(potato1)
potato1.cook(2)
print(potato1)
potato1.cook(9)
print(potato1)

















