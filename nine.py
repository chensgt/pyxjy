score = int(input("输入一个分数:"))
if 100 >= score >= 90:
    print(score, "A")
else:
    if 90 > score >= 80:
        print(score, "B")
    else:
        if 80 > score >= 60:
            print(score, "C")
        else:
            if 60 > score >=0:
                print(score, "D")
            else:
                print("输入错误")