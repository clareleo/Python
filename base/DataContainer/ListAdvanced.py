"""
使用while和for循环遍历列表
"""
def list_while_func():
    """
    使用while循环遍历列表的演示函数
    :return: None
    """
    mylist = ["song", "ming", "Python"]
    # 循环控制变量：通过下标索引来控制，默认0
    # 每一次循环将下标苏姚
    index = 0
    while index < len(mylist):
        # 通过index变量取出对应下标的元素
        element = mylist[index]
        print(f"列表的第{index + 1}个元素是：{element}")
        # 至关重要 将循环变量（index）每一次循环都+1
        index += 1

def list_for_func():
    """
    使用for循环遍历列表的演示函数
    :return:
    """
    mylist = ["song", "ming", "Python"]
    for index in range(len(mylist)):
        element = mylist[index]
        print(f"列表的第{index + 1}个元素是：{element}")
        index += 1

if __name__ == '__main__':
    list_while_func()
    list_for_func()