import random
secret = random.randint(1,10)
print('....我爱鱼C工作室......')
print("不妨猜一下小甲鱼现在心里想的是哪个数字:", end = "")
guess = 0
times = 3
while (guess !=secret) and (times > 0):
    temp = input ()
    
    if temp.isdigit():
        guess = int(temp)
        if guess == secret:
            print("我草,你是小甲鱼心里的蛔虫吗?!")
            print("哼,猜中了也没有奖励!")    
        else:
            if guess > secret:
                print("哥,大了大了~~~")
                print("再试一次吧")
                print("最后一次机会啦,好好把握哦:")
                times = times -1
            else:
                print("嘿,小了小了~~~")
                print("再试一次吧")
                print("最后一次机会啦,好好把握哦:")
                times = times -1
    else:
        print("抱歉,请输入一个整数:", end = "")
            
print("游戏结束,不玩啦")