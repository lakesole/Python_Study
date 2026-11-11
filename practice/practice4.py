#16.
person = {"name": "다윗", "age": 28, "job": "개발자"}

for i in person:
    print(i, ":", person[i])

#17.
for i in range(1, 101):
    if i % 15 == 0:
        print(i)
        
#18.
while True:
    number = int(input("숫자를 입력하세요"))
    if number == 0:
        print("종료!")
        break
    else:
        print("* " * number)
        
#19.
numbers = [-3, 5, -1, 8, -7, 2, 4, -9]
box = []

for i in numbers:
    if i >= 1:
        box.append(i)
print(box)

#20. 
min_num = None
while True:
    number = int(input("숫자를 입력하세요"))
    if number == 0:
        break
    if min_num is None or min_num > number:
        min_num = number
print(min_num)

#21.
words = ["사과", "수박", "파인애플", "딸기", "블루베리"]
longest = ""

for word in words:
    if len(word) > len(longest):
        longest = word
print(f"가장 긴 단어: {longest}")
    
#22.
a = [1, 2, 3]
b = [4, 5, 6]
box = []

for i in a:
    box.append(i)
for i in b:
    box.append(i)    
print(box)

#23.
fruits = []

while True:
    fruit = input("과일을 입력하세요 ")
    if fruit == "done":
        break
    fruits.append(fruit)
print(fruits)

#24.
numbers = [1, 2, 3, 2, 4, 3, 5, 1]
seen = []
duplicates =[]

for i in numbers:
    if i in seen:
        if i not in duplicates:
            duplicates.append(i)
    else:
        seen.append(i)
print(duplicates)

#25.
plus = 0
while True:
    number = int(input("숫자를 입력하세요"))
    if number == 0:
        break
    plus = plus + number
print(plus)

#26.
numbers = [-1, 2, -3, 4, -5, 6]
box = []

for i in numbers:
    if i > 0:
        box.append(i)
print(box)    

#27.
box = 1

for i in range(1, 11):
    box = box * i
print(box)