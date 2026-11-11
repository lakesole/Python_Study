def greet(name):
    print(f"안녕하세요, {name}!")
    
greet("다윗")
greet("철수")


def add(a, b):
    return a * b

result = add(4, 5)
print(result)

def introduce(name, age=20):
    print(f"저는 {name}이고 {age}살입니다.")
    
introduce("다윗")
introduce("다윗", "28")



def total(numbers):
    result = 0
    for i in numbers:
        result = result + i
        
    return result

total([1, 2, 3, 4, 5])


def average(numbers):
    total = 0
    for i in numbers:
        total = total + i
    return total / len(numbers)
 
print(average([10, 20, 30, 40, 50]))
   