for i in range(5):
    print(i)
    
fruits = ["사과", "바나나", "딸기"]

for fruit in fruits:
    print(fruit)
    
    
count = 0

while count < 5:
    print(count)
    count += 1

for i in range(10):
    if i == 5:
        break
    print(i)

while True:
    answer = input("종료하려면 q를 입력하세요:")
    if answer == "q":
        break
    print("계속 실행중...")
    
total = 0

for i in range(1, 11):
    total = total + i

print(total)
    
while True:
    number = int(input("숫자를 입력하세요"))
    if number == 0:
        break
    elif number % 2 == 0:
        print("짝수입니다")
    elif number % 2 == 1:
        print("홀수입니다")
    else:
        print("다시 입력해주세요")
    

