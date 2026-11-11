age = 20

if age >= 18:
    print("성인입니다")
else:
    print("미성년자입니다")
    

score = 85

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("F")

age = 20
has_ticket = True

if age >= 18:
    if has_ticket:
        print("입장 가능")
    else:
        print("티켓이 없습니다")
else:
    print("미성년자는 입장 불가")
 
x = 15

if x > 20:
    print("A")
elif x > 10:
    print("B")
elif x > 5:
    print("C")
else:
    print("D")


score = int(input("점수를 입력하세요."))

if score >= 90:
    print("A등급")
elif score >= 80:
    print("B등급")
elif score >= 70:
    print("C등급")
else:
    print("D등급")
    
age = int(input("나이를 입력하세요"))

if age >= 13 and age <= 19:
    print("청소년입니다")
else:
    print("청소년이 아닙니다")