# 新建列表
bri = set(['brazil', 'russia','india'])

# 测试成员资格
def test(member):
    if member in bri:
        print('ture')
    else:
        print('false')
test('india')
test('china')
print('\n')

# 基本集合操作(复制，子集，交集)
bric = bri.copy()
bric.add('china')
if bric.issuperset(bri):
    print('ture')
else:
    print('false')
print('\n')
brid = bri.copy()
brid.remove('india')
print(bri & brid )
print('\n')

# 指针操作：copy方法是复制一个对象，而直接使用表达式则是创造一个实例

print(bri)
print(bric)
brie = bric
print(brie)
print('\n')
brie.remove('russia')
print(bri)
print(bric)
print(brie)

# P.S. Set仅着重于 intersection 是否存在而不在乎其顺序与出现次数
# 因而每次编译执行，在输出结果次序上都会可能不尽相同
# 然而 intersection 的存在状态都是相同的