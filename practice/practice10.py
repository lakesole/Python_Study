#1.
import math

print(math.sqrt(16))
print(round(math.pi, 2))
print(math.ceil(10))
print(math.floor(10.9))

#2.
import random

print(random.randint(1,10))

#3.
import random

fruits = ["사과", "바나나", "딸기", "포도"]

print(random.choice(fruits))

#4.
from datetime import datetime

now = datetime.now()
print(f"오늘은 {now.year}년 {now.month}월 {now.day}일입니다.")

#5.
import random

total = []
for i in range(5):
    number = random.randint(1, 100)
    total.append(number)
    
print(total)


#6.
import random

choices = ["가위", "바위", "보"]

print(random.choice(choices))

#7.
import math

print(math.pow(2, 10))

#8.
from datetime import datetime

now = datetime.now()

print(f"현재 시각: {now.hour}시 {now.minute}분 {now.second}")

#9.
import random

numbers = [1, 2, 3, 4, 5]

random.shuffle(numbers)

print(numbers)

#10.
import math, random

number = random.randint(1, 100)
sq = round(math.sqrt(number), 2)

print(f"랜덤숫자: {number}, 제곱근: {sq}")

#11.
import random

number = random.sample(range(1, 46), 6)
print(number)

#12.
from datetime import datetime

days = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]
now = datetime.now()

today = days[now.weekday()]
print(f"오늘은 {today}입니다.")

#13.
import math

number = math.fabs(int(input("숫자를 입력하세요.")))
print(number)

#14.
import random

answer = ["앞면!", "뒷면!"]

print(random.choice(answer))

#15.
import os
print(os.getcwd())

#16.
import random

answer = random.randint(1, 10)
number = int(input("숫자를 입력하세요 "))

if number == answer:
    print("정답!")
else:
    print("오답!")
    
#17.
import math
a = 3 
b = 4
answer = math.sqrt((a ** 2) + (b ** 2))

print(f"빗변: {answer}")

    
#18.
from datetime import datetime

now = datetime.now()
print(now.strftime("%Y-%m-%d"))

#19.
import random

fruits = ["사과", "바나나", "딸기", "포도", "수박", "키위"]

answer = random.sample(fruits, 3)
print(answer)

#20.
from datetime import datetime
import math, random

now = datetime.now()
today = now.strftime("%Y-%m-%d")

number = random.randint(1,101)

sq = math.sqrt(number)

print(f"오늘: {today}\n 랜덤숫자: {number}\n 제곱근: {sq}")

#21.
import random

choices = ["가위", "바위", "보"]
computer = random.choice(choices)
me = input("가위,바위,보 중 선택: ")

print(f"나: {me}")
print(f"컴퓨터: {computer}")

if me == computer:
    print("비겼어요!")

elif (me == "가위" and computer == "보") or \
     (me == "바위" and computer == "가위") or \
     (me == "보" and computer == "바위"):
         print("이겼어요!")
else:
    print("졌어요!")

#22.
import math

radius = 5
a = round((math.pi) * (radius ** 2),2)
b = round(2 * (math.pi) * radius, 2)
print(f"넓이: {a}\n 둘레: {b}")

#23.
from datetime import datetime

now = datetime.now()
print(now.strftime("%Y년%m월%d일"))
print(now.strftime("%Y/%m/%d"))

#24.
import random

number = [1, 2, 3, 4, 5, 6, 7, 8, 9]

password = random.sample(number, 4)

print(password)

#25.
import math, random

radius = random.randint(1, 10)
area = math.pi * radius * radius
area = round(area, 2)

print(f"반지름: {radius},\n 넓이: {area}")


#26.
import random
number = random.randint(1, 100)
while True:
    print(number)
    me = int(input("숫자를 입력하세요: "))
    if number > me:
        print("더 큰 숫자!")
        continue
    elif number < me:
        print("더 작은 숫자!")
        continue
    elif number == me:
        print("정답!")
        break
    
#27.
from datetime import datetime

days = ["평일", "평일", "평일", "평일", "평일", "주말", "주말",]
now = datetime.now()

today = days[now.weekday()]
print(f"오늘은 {today}입니다!")

#28.
import math

numbers = [4, 9, 16, 25, 36]
answer = []

answer = [math.sqrt(i) for i in numbers] 
print(answer)
    
#29.
import math, random
average = 0

numbers = random.sample(range(1, 100), 5)
average = sum(numbers) / len(numbers)

print(f"숫자들: {numbers}, 평균: {average}")

#30.
from datetime import datetime

month = ["상반기", "하반기"]
now = datetime.now()

if now.month <= 6:
    print("상반기 입니다!")
else:
    print("하반기 입니다!")