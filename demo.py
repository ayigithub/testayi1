print("hello,world")
print(True)
print([])
print({},{2},[])

name="阿燚"
print("你好,{}".format(name))
print("你好, {}".format(name))
"""zhushi"""
"""print("1"+"2")
print((14+37)/7+99/3)
name=input("输入您的姓名：")
print(name)"""

"""a=float(input("输入数字1："))
b=float(input("输入数字2："))
c=a+b
print(c)
print(type(c))"""

"""a=input("请输入内容：")
print(len(a))"""

a=("n","啊哈哈",3,33,56,True,7,7,7,False)
print(a)
print(a[0])
print(a.index(7))
print(a.count(0))

b=["hahaha","k",324,1,1,5]
print(b)
b.append(9)
print(b)
b.insert(2,6)
print(b)

xx={"name":"阿燚","age":17}
print(xx["age"])

print("\n".join([''.join([('chenchen'[(x-y)%8]if((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0 else' ')for x in range(-30,30)])for y in range(15,-15,-1)]))