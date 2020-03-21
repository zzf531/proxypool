class Animal(object):
    def run(self):
        print('Animal is running...')


class Dog(Animal):
    def run(self):
        print('Dog is running...')


class Cat(Animal):

    def run(self):
        print('Cat is running...')





def run_twice(animal):
    animal.run()
    animal.run()


run_twice(Dog())