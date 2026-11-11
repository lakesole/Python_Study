#파일 읽기
with open("test.txt", "r") as f:
    content = f.read()
    print(content)
    
#파일 쓰기
with open("test.txt", "w") as f:
    f.write("안녕하세요!\n")
    f.write("파이썬 공부 중입니다.\n")
    
try:
    number = int(input("숫자를 입력하세요: "))
    print(10/ number)
except ValueError:
    print("숫자가 아닙니다")
except ZeroDivisionError:
    print("0으로 나눌 수 없어요")
    
try:
    f = open("test.txt", "r")
    content = f.read()
except FileNotFoundError:
    print("파일이 없어요")
finally:
    print("항상 실행돼요")

#1
with open("hello.txt", "w") as f:
    f.write("파이썬 공부 중!\n")
    f.write("오늘도 화이팅!\n")

with open("hello.txt", "r") as f:
    content = f.read()
    print(content)

#2
try:
    number = int(input("숫자를 입력하세요: "))
    print(100/ number)
except ValueError:
    print("숫자를 입력해주세요!")
except ZeroDivisionError:
    print("0으로 나눌 수 없어요!")