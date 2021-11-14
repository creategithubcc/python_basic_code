for i in range(1,6):
    if(i==2):
        print(f'第{i}个苹果有一条虫子，吃下一个')
        continue
    if i==4:
        print('吃饱了不吃')
        break
    print(f'正在吃第{i}个苹果')