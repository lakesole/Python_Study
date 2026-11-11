def check_number(number):
    if number > 0:
        print("양수")
    elif number < 0:
        print("음수")
    else:
        print("영")
    
check_number(5)
check_number(-7)
check_number(0)

def bigger(a, b):
    if a > b:
        return a
    else:
        return b

print(bigger(3, 7))
print(bigger(10, 4))
print(bigger(5, 5))
    
def welcome(name):
    return(f"안녕하세요, {name}님! 오늘도 화이팅!")
    
print(welcome("다윗"))
print(welcome("철수"))


def find_max(number):
    max_num = number[0]
    for n in number:
        if n > max_num:
            max_num = n
    return max_num

print(find_max([3, 1, 7, 2, 9, 4]))

def average(numbers):
    total = 0
    for i in numbers:
        total = total + i
    return total / len(numbers)

def find_max(numbers):
    max_num = numbers[0]
    for n in numbers:
        if n > max_num:
            max_num = n
    return max_num

def report(name, scores):
    print(f"{name}님의 점수: {scores}")
    print(f"평균: {average(scores)} ")
    print(f"최고점: {find_max(scores)}")
    
report("다윗", [80, 90, 70, 100])

def square(number):
    return number * number

print(square(4))

def smaller(a, b):
    if a > b:
        return b
    else:
        return a
    
def introduce(name, age):
    return f"{name}님은 {age}살 입니다."
    
print(introduce("다윗", 28))

def count_up(number):
    for i in range(number + 1):
        print(i)
        
count_up(5)

def get_evens(numbers):
    result = []
    for i in numbers:
        if i % 2 == 0:
            result.append(i)
    return result

print(get_evens([1, 2, 3, 4, 5, 6, 7, 8]))


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

a = int(input("첫 번째 숫자: "))
b = int(input("두 번째 숫자: "))

op = input("연산자 (+, -, *, /): ")

if op == "+":
    print(add(a, b))
elif op == "-":
    print(subtract(a, b))
elif op == "*":
    print(multiply(a, b))
elif op == "/":
    print(divide(a, b))
else:
    print("올바른 연산자를 입력하세요!")

