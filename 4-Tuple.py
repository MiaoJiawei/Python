# 主程序
zoo = ('python', 'elephent', 'penguin')
print(zoo)
new_zoo = ['apple']
print(new_zoo)
for index in range(len(zoo)):
    new_zoo.append(zoo[index])
    print(new_zoo)

# 列表嵌套元组
new_zoo.append(zoo)
print(new_zoo)

# 列表内索引
new_new_zoo=[]
for index in range(len(new_zoo)):
    if type(new_zoo[index]) == str:
        new_new_zoo.append(new_zoo[index])
    else:
        for index_l in range(len(new_zoo[index])):
            new_new_zoo.append(new_zoo[index][index_l])
print(new_new_zoo)

# 合并相同项
new_new_zoo = list(set(new_new_zoo))
print(new_new_zoo)

# 进行排序
new_new_zoo.sort()
print(new_new_zoo)