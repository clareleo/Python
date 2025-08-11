# 1.定义列表
from base.list.ListBase import index

list1 = [10, 20, 30]
print(f"列表元素为:{list1}")
# 2.追加数字
list1.append(40)
print(f"1.追加数字40后的列表元素为:{list1}")
# 3.追加一个新列表到列表末尾、
list2 = [50, 60, 70]
list1.extend(list2)
print(f"2.追加一个新列表到列表末尾后的列表元素为:{list1}")
# 4.取出第一个元素
element = list1.pop(0)
print(f"3.取出第一个元素后的列表元素为:{list1}\n4.取出的元素为:{element}")
# 5.取出最后一个元素
element = list1.pop()
print(f"5.取出最后一个元素后的列表元素为:{list1}\n6.取出的元素为:{element}")
# 6.查找元素40的索引值
index1 = list1.index(40)
print(f"7.查找元素40的索引值为:{index1}")