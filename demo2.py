class Person():
    name = 'ayi'
    age = 18

    def eat(self,food):
        print('吃{}'.format(food))
        return '吃完了'


p = Person()
print(p.eat('辣条'))