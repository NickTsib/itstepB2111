class Student:
    def __init__(self, name):
        self.name = name
        self.height = 160
        print('Hi!')


vasya = Student('Vasya')
print(vasya.height)
print(vasya.name)