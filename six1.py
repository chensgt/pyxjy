temp = input("不妨猜一下小甲鱼现在心里想的是哪个数字:")
while not isinstance(temp, int):
    print("抱歉,输入不合法")
    temp = input ("请输入一个整数:")