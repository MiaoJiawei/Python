# 定义字典
ab = {
    'Swaroop': 'swaroop@swaroopch.com',
    'Larry': 'larry@wall.org',
}

# 已知Key查找Value，基本操作
print("Swaroop's address is", ab['Swaroop'])
print('\nThere are {} contacts in the address-book\n'.format(len(ab)))

# 打印字典
def print_dict(ac):
    for name,address in ac.items():
        print('Contac {} at {}'.format(name,address))

# 添加Key-Value对
def add_dict(ad):
    name = input('name is: ')
    address = input('address is: ')
    ad[name] = address

# 删除Key-Value对
def del_dict(ae):
    name = input('name is: ')
    if name in ae:
        del ae[name]

# 判断错误输入
def judge(t):
    while True:
        l = input('input is wrong, exit programe?(yes/no)\n')
        if l == 'yes':
            print_dict(ab)
            return 1
        elif l == 'no':
            return 0
                
# 主程序
t = 0
while t == 0:
    operation = input('The operation you want to do:\n1.Print\n2.Add\n3.Delete\n')
    if operation == '1':
        print_dict(ab)
    elif operation == '2':
        add_dict(ab)
    elif operation == '3':
        del_dict(ab)
    else:
        t = judge(t)