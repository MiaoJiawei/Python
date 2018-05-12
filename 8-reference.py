print('Simple assignment')
shoplist = ['apple', 'mango', 'carrot', 'banana']

# 直接使用表达式将创造一个实例（将对象分配给变量，变量只会查阅（refer）某个对象，即将变量名称绑定（Binding）给对象

mylist = shoplist
print('mylist is ', mylist)
print('shoplist is ', shoplist)

del shoplist[0]

print('mylist is ', mylist)
print('shoplist is ', shoplist)

#使用切片方法可以获得一份复制

mylist = shoplist[:]
del mylist[0]

print('mylist is ', mylist)
print('shoplist is ', shoplist)

# 字符串对象操作
name = 'Swaroop'

if name.startswith('Swa'):
    print('YES, the string starts with "Swa"')
if 'a' in name:
    print('Yes, it contains the string "a"')
if name.find('war') != -1:
    print('yes, it cotains the string "war"')

delimiter = '_*_'
print(delimiter.join(mylist))