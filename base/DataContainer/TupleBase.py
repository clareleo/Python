# 定义元组 -- 元组和列表的区别就是元组不可修改
t1 = (1, "Hello", True)
t2 = ()
t3 = tuple()
print(f"1.t1的类型是：{type(t1)}, 内容是：{t1}")
print(f"2.t2的类型是：{type(t2)}, 内容是：{t2}")
print(f"3.t3的类型是：{type(t3)}, 内容是：{t3}")
# 定义单个元素的元素
t4 = ("hello",) # 元组中只有一个元素，必须加逗号
print(f"4.t4的类型是：{type(t4)}, t4的内容是：{t4}")
# 元组的嵌套
t5 = ((1, 2, 3), (4, 5, 6))
print(f"5.t5的类型是：{type(t5)}, 内容是：{t5}")

# 下标索引去取出内容
num = t5[1][2]
print(f"6.从嵌套元组中取出的数据是：{num}")
# 元组的操作：index查找方法
t6 = ("7.ming", "song", "Python")
index = t6.index("song")
print(f"8.song，的下标是：{index}")
# 元组的操作：count统计方法
t7 = ("ming", "song", "song", "song", "Python")
num = t7.count("song")
print(f"9.song：{num}个")
# 元组的操作：len函数统计元组元素数量
t8 = ("ming", "song", "song", "song", "Python")
num = len(t8)
print(f"10.t8元组中的元素有：{num}个")
# 元组的遍历：while
index = 0
while index < len(t8):
    print(f"while查询{index + 1}.元组的元素有：{t8[index]}")
    # 至关重要
    index += 1

# 元组的遍历：for
for element in t8:
    print(f"for查询元组的元素有：{element}")

# 修改元组内容
# t8[0] = "itcast"

# 定义一个元组
t9 = (1, 2, ["itheima", "itcast"])
print(f"11.t9的内容是：{t9}")
t9[2][0] = "song"
t9[2][1] = "ming"
print(f"12.t9的内容是：{t9}")
