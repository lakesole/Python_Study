#1.
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        print(f"{self.name}이 짖습니다: 왈왈!")

dog1 = Dog("초코", 3)
dog1.bark()

#2.
class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed
    
    def info(self):
        print(f"브래드: {self.brand}, 속도: {self.speed}")

car1 = Car("현대", 100)
car1.info()

#3.
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return(self.width * self.height)
    
    def perimeter(self):
        return((self.width + self.height) * 2)
    
r = Rectangle(5, 3)
print(r.area())
print(r.perimeter())

        
        
#4.
class Counter:
    def __init__(self):
        self.count = 0
        
    def up(self):
        self.count = self.count + 1
    
    def down(self):
        self.count = self.count - 1
    
    def show(self):
        print(self.count)
    
c = Counter()
c.up()
c.up()
c.up()
c.down()
c.show()



#5. 안녕하세요, 다윗입니다!, 안녕하세요, 철수입니다! self.name은 name이고 self가 있으므로 객체에 추가할수 있음. 그래서 다윗과 철수가 self.name에 들어가게 되어 답안이 나옴
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"안녕하세요, {self.name}입니다!")

p1 = Person("다윗")
p2 = Person("철수")
p1.greet()
p2.greet()

#6.
class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return(self.radius * self.radius * 3.14)
    
    
c = Circle(5)
print(c.area()) 
    
    
#7.
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
    def average(self):
        return(sum(self.score) / len(self.score))
    
    def show(self):
        print(f"{self.name}의 평균: {sum(self.score) / len(self.score)}")
    
s = Student("다윗", [80, 90, 100])
s. show()


#8.
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"{amount}원 입금완료")
        
    def withdraw(self, amount):
        if amount > self.balance:
            print("잔액 부족!")
        else:
            self.balance = self.balance - amount
            print("출금 완료!")
            
acc = BankAccount("다윗")
acc.deposit(10000)
acc.withdraw(3000)
acc.withdraw(20000)

#9.
class Thermometer:
    def __init__(self, celsius):
        self.celsius = celsius
        
    def to_fahrenheit(self):
        return(self.celsius * 9/5 +32)

t = Thermometer(100)
print(t.to_fahrenheit()) 
        
#10.
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name}이 먹습니다")

class Dog(Animal):
    def bark(self):
        print(f"{self.name}이 짖습니다: 왈왈!")

dog = Dog("초코")
dog.eat()
dog.bark()

#답: 초코이 먹습니다, 초코이 짖습니다: 왈왈! 
#이유: __init__으로 self객체를 받을수 있고, eat에서 self.name에 dog = Dog이 초코이므로
#self.name이 초코가 되었음

 #11.
class Calculator:
    def __init__(self):
         self.result = 0
    
    def add(self, n):
        self.result = self.result + n
        
    def subtract(self, n):
        self.result = self.result - n
    
    def reset(self):
        self.result = 0
    
    def show(self):
        print(self.result)
        
calc = Calculator()
calc.add(10)
calc.add(5)
calc.subtract(3)
calc.show()   # 12
calc.reset()
calc.show()   

#12.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def is_adult(self):
        if self.age >= 18:
            return(True)
        else:
            return(False)
    
    def introduce(self):
        print(f"저는 {self.name}이고 {self.age}살입니다.")
        
p = Person("다윗", 28)
print(p.is_adult())  # True
p.introduce() 

#13.
class Stack:
    def __init__(self):
        self.items = []
        
    
    def push(self, item):
        self.items = self.items + [item]
    
    def pop(self):
        self.items = self.items[:-1]
        
    def show(self):
        print(self.items)
        
s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.show()   # [1, 2, 3]
s.pop()
s.show() 

#14.
class Animal:
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        print(f"{self.name}이 먹습니다")
        
class Cat(Animal):
    def meow(self):
        print(f"{self.name}이 야옹!")
        
cat = Cat("나비")
cat.eat()   # 나비이 먹습니다
cat.meow()  # 나비이 야옹!

#15.
class Car:
    def __init__(self, brand):
        self.brand = brand
        self.speed = 0

    def accelerate(self, amount):
        self.speed += amount

    def info(self):
        print(f"{self.brand} 현재속도: {self.speed}")

car = Car("현대")
car.accelerate(50)
car.accelerate(30)
car.info()

'''
정답 : 현대 현재속도: 80
클래스 Car 만들고 그 안에 brand와 speed(accelerate) 함수를 넣음.
그후 speed 함수에 50, 30 두번 입력하여 총 80으로 출력되었고 브랜드도 현대로 입력하여
마지막 info함수에 brand, speed 를 출력하게 하였음
'''

#16.
class Wallet:
    def __init__(self, owner):
        self.owner = owner
        self.money = 0
    
    def add(self,amount):
        self.money = self.money + amount
        
    def spend(self, amount):
        if self.money < amount:
            print("돈이 부족해요!")
        elif self.money >= amount:
            self.money = self.money - amount
            
        
    def show(self):
        print(f"{self.owner}의 지갑: {self.money}원")
        
w = Wallet("다윗")
w.add(10000)
w.spend(3000)
w.spend(20000)  # 돈이 부족해요!
w.show()        
        
#17.
class Scoreboard:
    def __init__(self):
        self.score = []
    
    def add_score(self, score):
        self.score = self.score + [score]
        
    def highest(self):
        return(max(self.score))
    
    def average(self):
        score = self.score
        score_average = sum(score) / len(self.score)
        return(score_average)
    
    def show(self):
        print(self.score)
    
sb = Scoreboard()
sb.add_score(85)
sb.add_score(92)
sb.add_score(78)
sb.show()           # [85, 92, 78]
print(sb.highest()) # 92
print(sb.average()) # 85.0    

#18.
class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed
    
    def accelerate(self, amount):
        self.speed += amount
        
class ElectricCar(Car):
    def __init__(self, brand, speed,battery):
        self.brand = brand
        self.speed = speed
        self.battery = battery
    
    def charge(self):
        print("배터리 충전완료!")

ec = ElectricCar("테슬라", 0, 100)
ec.accelerate(50)
ec.charge()

#19.
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("...")

class Dog(Animal):
    def sound(self):
        print(f"{self.name}: 왈왈!")

class Cat(Animal):
    def sound(self):
        print(f"{self.name}: 야옹!")

dog = Dog("초코")
cat = Cat("나비")
dog.sound()
cat.sound()

'''
정답: 초코: 왈왈!, 나비: 야옹!
이유는 Animal 클래스에서 함수를 상속받았음.
self.name을 받고 sound함수를 상속받아 
사용하였음.
'''

#20.
class TodoList:
    def __init__(self):
        self.todo = []
    
    def add(self, todo):
        self.todo.append(todo)
        
    def done(self, index):
        self.todo.pop(index)
    
    def show(self):
        print(self.todo)
        
t = TodoList()
t.add("파이썬 공부")
t.add("운동하기")
t.add("책 읽기")
t.show()    # ['파이썬 공부', '운동하기', '책 읽기']
t.done(0)   # 첫 번째 삭제
t.show()    # ['운동하기', '책 읽기']