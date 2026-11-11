class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def bark(self):
        print(f"{self.name}이 짖습니다: 왈왈!")
        
    def info(self):
        print(f"이름: {self.name}, 나이: {self.age}살")
        
        
dog1 = Dog("초코", 3)
dog2 = Dog("바둑이", 5)

dog1.bark()
dog2.bark()
dog2.info()
dog1.info()


#문제
#1.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        print(f"저는 {self.name}이고 {self.age}살입니다.")

p = Person("다윗", 28)
p.introduce()


#2.

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"입금완료. 잔액: {self.balance}원")
        
    def withdraw(self, amount):
        if amount > self.balance:
            print("잔액이 부족합니다")
        else:
            self.balance = self.balance - amount
            print(f"출금완료. 잔액: {self.balance}원")        
    
        
account = BankAccount("다윗")
account.deposit(10000)
account.withdraw(3000)

class Cat:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def meow(self):
        print(f"{self.name} 고양이가 야옹!")

cat1 = Cat("나비", "흰색")
cat2 = Cat("치즈", "노란색")

cat1.meow()
cat2.meow()
        
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def show(self):
        print(f"{self.name}의 점수: {self.score}점")
    def is_pass(self):
        if self.score >= 60:
            print("합격!")
        else:
            print("불합격!")
            
s1 = Student("다윗", 85)
s2 = Student("철수", 45)

s1.show()
s1.is_pass()
s2.show()
s2.is_pass()
        