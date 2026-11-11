#day3
#1.답은 2,4,6
for i in range(2, 8, 2):
    print(i)
    
#2.

total = 0
for i in range(1, 51):
    total = total + i
print(total)

#3.
count = 1

while count < 11:
    print(count)
    count += 1

#4.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in numbers:
    if i % 2 == 0:
        print(i)

#5.
total = 0
while True:
    number = int(input("숫자를 입력해주세요"))
    if number == 0:
        break
    total = total + number
print(total)

#1.
for i in range(1, 11):
    if i % 2 == 1:
        print(i)
        
#2.
count = 100
while count > 50:
    count -= 1
print("50 도달!")

#3.
count = 0
while True:
    word = input("단어입력 (quit으로 종료): ")
    if word == 'quit':
        break
    count += 1
print(f"총 {count}개 입력했어요!")
        
#4.
total = 0
numbers = [3, 15, 7, 22, 8, 11, 4, 19]

for i in numbers:
    if i > 10:
        total = total + i
print(total)
        
#5.
while True:
    number = int(input("숫자를 입력하세요"))
    if number == 0:
        print("종료!")
        break    
    elif number >= 1:
        print("양수!")
    elif number < 0:
        print("음수!")    

#6.
for i in range(1, 10):
    print(f"3 x {i} = {3 * i}")
    
#7.
for dan in range(2, 5):
    for i in range(1, 10):
        print(f"{dan} x {i} = {dan * i}")

#8.
number = 0
while True:
    plus = int(input("숫자를 입력하세요 "))
    if plus == 0:
        break
    elif plus % 2 == 0:
        number = number + plus
    
print(f"짝수 합계: {number}")

#9.
fruits = ["사과", "딸기", "바나나", "포도", "수박"]

for i, fruit in enumerate(fruits, 1):
    if fruit == "바나나":
        print(f"바나나 {i}번째에 있어요!")
        
#10.
max_num = 0
while True:
    number = int(input("숫자를 입력하세요"))
    if number == 0:
        break
    if number > max_num:
        max_num = number
print(f"최댓값: {max_num}")

#11.
numbers = [1, 2, 3, 4, 5]
total = 1
for i in numbers:
    total = total * i
print(total)

#12.
while True:
    word = input("단어를 입력하세요 ")
    if word == "quit":
        print("종료!")
        break
    else:
        print(f"뒤집기: {word[::-1]}")
        
#13.
for i in range(1, 6):
    print("*" * i)
    
#14.
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

numbers = set(numbers)
print(f"중복제거 후 개수: {len(numbers)}개")
    
#15.
while True:
    number = int(input("숫자를 입력하세요"))
    if number == 0:
        print("종료!")
        break
    elif number % 15 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)     


        