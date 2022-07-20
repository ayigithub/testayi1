class Person():
    name = 'ayi'
    age = 18
    sex = '男'

    def eat(self,food):
        print('吃{}'.format(food))
        return '吃完了'
    
    def __init__(self,sex,highth):
        self.sex = sex
        self.highth = highth


p = Person('女',177)
print(p.eat('辣条'))
print(p.sex)
print(p.highth)