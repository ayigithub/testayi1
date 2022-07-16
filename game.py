# import random
# from practice import my_abs
# # print("------game------")
# # a=input("请输入您的姓名：")
# # print("你好,"+a+"!")

# # print('--------猜数游戏--------')

# # a = 1
# # b = random.randint(0,10)
# # while a<=3:
# #     guess = int(input("请猜测一个数字:"))
# #     if guess == b:
# #         print("猜对啦!")
# #         print('游戏结束！')
# #         break
# #     elif guess > b:
# #         print('哦哦，有点大了哦')
# #     else:
# #         print('小啦！')    
# #     a = a+1
# #     if a>3:
# #         print("次数用完了哦，游戏结束！")
# #         break

# # secret = random.randint(0,10)
# # guess = int(input("猜测一个数字："))
# # while guess != secret:
# #     guess = int(input("错啦，再猜一次吧："))
# #     if guess > secret:
# #         print ("大了大了")
# #     else:
# #         print ("小了")
# # print("猜对啦！")
# # print ("游戏结束，不玩啦！")


# # number=random.randint(1,10)
# # count=0

# # while count<3:
# #     temp=input("please guess a number:")
# #     guess=int(temp)
# #     count+=1

# #     if guess==number:
# #         print("u are right")
# #         break   
# #     elif guess>number:
# #         print("it is not right")
# #         print("please guess a smaller number")
# #     else:
# #         print("it is not right")
# #         print("guess a larger number")       
# #     if count>=3:
# #         print("times out")

# # print("end")

# print(my_abs(-99))


# a = str(input('请输入：'))
# b = str(input(''))
# print(a + b)

# a = input('请输入：')
# b = input('请输入：')
# c = len(a) + len(b)
# print(c)


# a = (1,'d','lll')
# print(a[1:])
# print(len(a))

# a = [1,'a','哈哈哈']
# a.append('la')
# a.insert(0,'wy')
# b = a.pop(2)
# print(a)
# print(b)

# a = input('请输入姓名：')
# b = input('年龄：')
# c = input('性别：')
# aa = {}
# aa['name'] = a
# aa['age'] = b
# aa['sex'] = c
# print(aa)

# b = 18
# if b > 18:
#     print('成年')
# else:
#     print('未成年')


# db = [{'name':'123','password':'12345'},{'name':'1234','password':'12345'}]
# zh = input('请输入账号：')
# mm = input('请输入密码：')
# a = 0
# for i in db:
#     a = a + 1
#     if zh == i.get('name') and mm == i.get('password'):
#         print('账号{}，登陆成功'.format(zh))
#         break
#     else:
#         if a < len(db):
#             continue
#         else:
#             print('登陆失败')


db = [{'uname':'123','pwd':'12345'},{'uname':'1234','pwd':'123456'}]
zh = input('请输入账号：')
mm = input('请输入密码：')

a = 1 

for i in db:
    while a <= len(db):
        a = a + 1
        if zh == i.get('uname'):
            i['pwd'] = mm
            break
        else:
            db.append({'uname':zh,'pwd':mm})

print(db)