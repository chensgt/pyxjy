import random
secret = random.randint(1, 10)
times = 0
while True:
    if times == 3:
        print('>>>>>>>>>>>次数已用尽')
        break
    guess = int(input('请输入: '))
    if guess == secret:
        print('猜对了!')
        break
    elif  guess > secret:
        print('大了!')
    else:
        print('小了!')
    times += 1
    
