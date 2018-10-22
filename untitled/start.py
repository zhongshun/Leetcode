class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(object ):
    def drun(self):
        print('Dog is running...')

class Cat(Animal, Dog):
    pass

p = Cat()
p.drun()
