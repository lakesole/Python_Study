#1.
with open("hello.txt", "w")as f:
    f.write("안녕하세요!\n")
    f.write("파이썬 공부 중입니다.\n")
    
#2.
with open("hello.txt", "r")as f:
    content = f.read()
    print(content)
    
#3.
try:
    number = int("abc")# "abc"는 정수가 아니기때문. 
except ValueError:
    print("숫자가 아닙니다.")

    
#4.
try:
    number = int(input("숫자를 입력하세요"))
    total = 100 / number
    print(total)
except ValueError:
    print("숫자를 입력해주세요!")
except ZeroDivisionError:
    print("0으로 나눌수 없어요!")
    
#5.
with open("hello.txt", "a") as f:
    f.write("추가된 내용입니다.")
    
with open("hello.txt", "r") as f:
    content = f.read()
    print(content)
    
#6.
numbers = [1, 2, 3, 4, 5]

with open("numbers.txt", "w")as f:
    for i in numbers:
        f.write(str(i)+ "\n")

with open("numbers.txt", "r")as f:
    print(f.read())
    
#7.
try:
    with open("abc.txt", "r")as f:
        content = f.read()
except FileNotFoundError:
    print("파일이 존재하지 않아요!")
    
#8.
fruits = ["사과", "바나나", "딸기"]

try:
    number = int(input("숫자를 입력하세요: "))
    print(fruits[number])
except IndexError:
    print("범위를 벗어났어요!")
    
#9.
try:
    number = int(input("숫자를 입력해주세요: "))
    print(f"결과: {1000 / number}")
except ZeroDivisionError:
    print("0으로 나눌 수 없어요!")
finally:
    print("항상 실행돼요!")

#10.
scores = [85, 90, 78, 92, 88]

with open("score.txt", "w")as f:
    for score in scores:
        f.write(str(score) + "\n")

with open("score.txt", "r")as f:
    lines = f.readlines()
    numbers = [int(line.strip()) for line in lines if line.strip()]
    print(f"평균: {sum(numbers) / len(numbers)}")
    
#11
with open("my_file.txt", "w")as f:
    f.write("다윗")

with open("my_file.txt", "r")as f:
    print(f.read())
    
#12.
fruits = ["사과", "바나나", "딸기", "포도"]

with open("fruits.txt", "w")as f:
    for fruit in fruits:
        f.write(fruit + "\n")

with open("fruits.txt", "r")as f:
    print(f.read())
    
#13.
with open("fruits.txt", "a")as f:
    f.write("수박" + "\n")

with open("fruits.txt", "r")as f:
    print(f.read())
    
#14.
try:
    with open("없는파일.txt", "r")as f:
        print(f.read())
except FileNotFoundError:
    print("파일을 찾을 수 없어요!")
    
#15.
try:
    number = int(input("숫자를 입력하세요: "))
    print(f"결과: {100 / number}")
except ZeroDivisionError:
    print("0으로 나눌 수 없어요!")
except ValueError:
    print("숫자를 입력해주세요!")
    
#16.
try:
    number = int(input("숫자를 입력하세요: "))
    print(f"결과: {1000 / number}")
except ZeroDivisionError:
    print("0으로 나눌 수 없어요!")
except ValueError:
    print("숫자를 입력해주세요!")
finally:
    print("프로그램 종료!")

#17.
scores = [85, 92, 78, 96, 88]

with open("scores.txt", "w")as f:
    for score in scores:
        f.write(str(score) + "\n")

with open("scores.txt", "r")as f:
    numbers = [int(line.strip()) for line in f.readlines() 
               if line.strip()]
    max_score = numbers[0]
    for n in numbers:
        if n > max_score:
            max_score = n
    print(f"최고점: {max_score}")
    
#18.
numbers = [1, 2, 3, 4, 5]
with open("numbers.txt", "w")as f:
    for i in numbers:
        f.write(str(i) + "\n")

with open("numbers.txt", "r")as f:
    number = [int(line.strip()) for line in f.readlines()
                if line.strip()]
    print(sum(number))

#19.
with open("name.txt", "w")as f:
    name = input("이름을 입력하세요: ")
    f.write(name)

with open("name.txt", "r")as f:
    save = f.read()
    print(f"{save}님 환영합니다!")
     

#20.
with open("todo.txt", "a")as f:
    while True:
        todo = input("할일을 입력하세요: ")
        if todo == "done":
            break
        f.write(todo + "\n")
        
        
with open("todo.txt", "r")as f:
    savetodo = f.read()
    print(f"=== TO DO ===\n {savetodo}")