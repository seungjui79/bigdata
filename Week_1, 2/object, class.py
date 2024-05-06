import os
os.system('clear')

#클래스 선언 
class Dog:
    name = 'defalut'
    gender = 'Male/Female'
    owner = 'defalut name'

    def Bark(self):
        print(self.name + ': 멍멍')

# 객체 생성과 사용 방법
        dog = Dog()
        dog.name = "노랑이"
        dog.gender = 'Female'
        dog.owner = 'J.Kim'
        dog.Bark()