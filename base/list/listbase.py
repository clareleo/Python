mylist = ["itcast", "itheima", "python"]
print(f"列表元素为:{mylist}")
# 列表的索引
index = mylist.index("itheima")
print(f"1.itheima在列表中的下标索引值是:{index}")
# 如果查找的元素不存在，则返回-1（报错）
# print(mylist.index("itheima1"))
# 修改特定下标索引的值
mylist[0] = "铭铭"
print(f"2.正向第0位下标索引值修改后为:{mylist[0]}")
# 3.在指定下标位置插入新元素
mylist.insert(1, "bast")
print(f"3.列表第1位插入元素后结果是:{mylist}")
# 4.在列表末尾追加新元素,单个
mylist.append("4")
print(f"4.列表末尾追加元素后结果是:{mylist}")
# 5.在列表末尾追加新元素,多个
mylist2 = ["5", "6"]
mylist.extend(mylist2)
print(f"5.列表末尾追加两个元素后结果是:{mylist}")
# 6.删除列表元素
mylist = ["itcast", "itheima", "python", "itcast"]
print(f"列表元素为:{mylist}")
mylist.remove("itcast") # 删除列表中第一个值为itcast的元素
print(f"6.删除列表元素后结果是:{mylist}")
# pop 的原理是取出列表指定索引内容
element = mylist.pop()    # 取出列表末尾元素,也可指定删除的元素索引
print(f"7.删除列表末尾元素后结果是:{mylist}\n8.取出后的元素在列表中的索引位置是:{element}")
del mylist[0]
print(f"9.删除列表指定元素后结果是:{mylist}")
mylist.clear()
print(f"10.清空列表后结果是:{mylist}")
# 11.统计某个元素在列表出现的数量 count
mylist = ["itcast", "itheima", "python", "itcast"]
print(f"列表元素为:{mylist}\n11.元素itcast出现的次数是:{mylist.count('itcast')}")
# 12.列表长度
print(f"12.列表长度是:{len(mylist)}")