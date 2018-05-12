# 购买=查询列表，存在输入项则删除，不存在则提示
def bought(shoplist):
    have = True
    bought = input('bought ')
    for index in range(len(shoplist)):
        if bought == shoplist[index]:
            print('bought ',shoplist[index])
            del shoplist[index]
            have = False
    while have:
        print('don\'t have this plane')
        break
        
# 添加列表
def add(shoplist):
    add = input('add: ')
    print('now, have to buy: ',add)
    shoplist.append(add)

# 主程序
shoplist = ['apple','mango','carrot','banana']
print('now the list: ',shoplist)
while True:
    getchar = input('add or buy: ')
    if getchar == 'add':
        add(shoplist)
        print('now the list: ',shoplist)
    elif getchar == 'bought':
        bought(shoplist)
        print('now the list: ',shoplist)
    else:
        print("unacceptable command")
        break
print('now the list: ',shoplist)