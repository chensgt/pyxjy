temp = input("请输入年份:")
years = int(temp)
if years/400 == int(years/400):
    print(temp + "是闰年!")
else:
    if (years/4 == int(years/4)) and (years/100 != int(years/100)):
        print(temp + "是闰年!")
    else:
        print(temp + "不是闰年!")
            

