def example_for():
    for i in range(10):
        if i == 5:
            print('Loop was broken.')
            break
        # 如果换成continue则两句话都会输出
        else:
            print('program continues to execute.')
        # 如果程序被终止，否则输出下面这段
    # for或while循环里的else语句只为循环服务，是用来判断循环是否完成，循环未被打断就输出else
    else:
        print('Loop executed perfectly!')


def example_while():
    i: int = 0
    is_connected = True

    while is_connected:
        if i == 5:
            # 必须让它变成false，无论是break还是其他都不行
            is_connected = False
            # 用break或是其他结束语句的话，是不会执行else的

        i += 1
    else:
        print('Else block was executed!')


if __name__ == "__main__":
    example_for()
    example_while()
