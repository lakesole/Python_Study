#1.
x = 10
y = "20"
print(x + int(y))

#2.
name = "다윗"
age = 28
print(f"안녕하세요! 저는 {name}이고, {age}살입니다.")

#3.
a = "5"
b = "3"

print(a + b)
#답은 53. ""를 썼기 때문에 숫자가 아닌 텍스트로 인식하기 때문


#4.
a = int(input("첫번쨰 숫자"))
b = int(input("두번째 숫자"))

print(a + b)

#5.
print(type(100), type(3.14), type("hello"), type(True), type([1, 2, 3]))

#6.
print(type(int("42")))#class 'int'
print(type(float("3.14")))#class 'float'

#7.
name = input("이름을 입력하세요: ")
name_number = len(name)
print(f"{name}님 환영합니다! 이름은 {name_number}글자네요.")

#8.
a = 10
b = 3
print(a // b)
print(a % b)
print(a ** b)

#9.
tall = float(input("키를 입력하세요(cm): "))
m = tall / 100
print(f"키: {m}m")

#10.
apple = "사과"
apple_price = 1500
banana = "바나나"
banana_price = 800
total = apple_price + banana_price

print(f"{apple}의 가격은 {apple_price}원이고, {banana}의 가격은 {banana_price}원입니다.")
print(f"두 과일의 합계는 {total}원입니다.")


#day2문제
#1. 답은 A
x = 15
if x > 10:
    print("A")
elif x > 5:
    print("B")
else:
    print("C")

#2.
number = int(input("숫자를 입력하세요"))
if number > 0:
    print("양수")
elif number < 0:
    print("음수")
else:
    print("영")

#3.
age = int(input("나이를 입력하세요"))
if 0 < age <= 12:
    print("어린이")
elif 13 <= age <= 18:
    print("청소년")
elif 19 <= age <= 64:
    print("성인")
else:
    print("노인")
    
#4.
a = 10
b = 20
if a > 5 and b > 15:
    print("A")
elif a > 5 or b > 25:
    print("B")
else:
    print("C")
"""
답은 A, 이유는 
A가 나올경우는 a가 5 이상이고, b가 15이상일때
B가 나올경우는 a가 5 이상 또는 b가 25이상일때
C가 나올경우는 위에 경우 이외
현재 a는 10, b는 20 이므로 해당하는 그룹은 A이므로
답은 A
"""

#5.
user_id = "admin"
user_password = "1234"
id = input("아이디를 입력하세요")
password = input("비밀번호를 입력하세요.")

if id == user_id and password == user_password:
    print("로그인 성공!")
else:
    print("로그인 실패!")

#6.
score = int(input("점수를 입력하세요"))
if score >= 90:
    print("A등급 - 훌륭해요!")
elif score >= 80:
    print("B등급 - 잘했어요!")
elif score >= 70:
    print("C등급 - 괜찮아요!")
elif score >= 60:
    print("D등급 - 조금 더 노력해요!")
else:
    print("F등급 - 분발하세요!")

#7.
month = int(input("월을 입력하세요"))
if month in [3, 4, 5]:
    print("봄")
elif month in [6, 7, 8]:
    print("여름")
elif month in [9, 10, 11]:
    print("가을")
else:
    print("겨울")
    
#8.
a = int(input("첫번째 숫자를 입력해주세요"))
b = int(input("두번째 숫자를 입력해주세요"))
if a % b == 0:
    print("배수입니다!")
else:
    print("배수가 아닙니다!")

#9.
a = int(input("첫번째 숫자를 입력해주세요"))
b = int(input("두번째 숫자를 입력해주세요"))
c = int(input("세번째 숫자를 입력해주세요"))

if a >= b and a >= c:
    print(a)
elif b >= a and b >= c:
    print(b)
else:
    print(c)
    
#10.
x = 0
if x:
    print("A")
elif not x:
    print("B")
else:
    print("C")

"""
파이썬에서 0은 false로 인식 되기 때문에 0 그 자체는 거짓임.
그래서 if x: print("A")는 x가 0이기 때문에 거짓이 되어 나올수 없음.
그리고 다음 elif not x: print("B")는 not이 있기 때문에 0의 거짓을 참으로 만들어 주기 때문에
B가 정답
"""

#day3
#1. 


