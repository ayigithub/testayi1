
# from test.a import aa
# print(aa)


# a = [1,2,3]
# try:
#     print(a[3])
# except:
#     print('代码错误')


# def sum(a,b):
#     sum = a + b
#     return sum

# m = 1
# n = 2
# h = 3

# print(sum(m,n))
# print(sum(n,h))

# def test1(j = 10):
#     return j


# print(test1(1))
# print(test1())


# def test2():
#     return 10,20,30


# a, b ,c = test2()
# mm = test2()
# print(a,b,c)
# print(mm)


from dbtool import chaxun,commit


name = input('姓名：')
age = input('年龄：')


# # 查询是否存在
# sql = 'select * from basic_info where name = {} and age = {}'.format(name,age)
# if len(chaxun(sql)) == 0:
#     print('未添加')
# else:
#     print('已存在')


# 添加信息
sql1 = 'insert into basic_info values("{}","{}")'.format(name,age)
commit(sql1)
sql2 = 'select * from basic_info'
print(chaxun(sql2))