# 计算1到100的求和
# 加入分支结构实现1—100之间的偶数求和
# 使用python实现1-100之间的偶数求和

# result = 0
# for i in range(101):
#     print(i)
#     result = result+i
# print(result)

# result = 0
# for i in range(101):
#     if i%2==0:
#        result = result + i
# print(result)

# result = 0
# for i in range(0,101,2):
#        result = result + i
# print(result)

# while语句
# a = 1
# while a == 1:
#     print("a=1")
#     a = a+1
# else:
#     print("a!=1")
#     print(a)

# break 和 continue
# for i in range(1,10):
#     if i==5:
#        continue
#     print (i)

# 猜数字游戏
# 计算机出一个1~100之间的随机数由人来猜
# 计算机根据人猜的数字分别输出提示 大一点/小一点/猜对了
import random
count = 0
while True:
    if count > 0:
        answer = str(input("是否要继续，输入y/n:"))
        if answer == 'n':
            print("游戏结束！")
            break
    num = random.choice(range(100)) + 1
    a = 0
    while a != num:
        a = int(input("请输入您猜的数字："))
        if a > num:
            print("太大了")
        elif a < num:
            print("太小了")
    else:
        print("恭喜您猜对了!")
    count += 1
