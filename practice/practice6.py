#1.
numbers = [1, 2, 3, 4, 5, 6, 7]

print(numbers[2:5])

#2.
fruits = ["사과", "바나나", "딸기"]
fruits.append("포도")
fruits.remove("바나나")
print(fruits)

#3.
person = {"name": "다윗", "age": 28, "city": "서울"}
print(f"저는 {person['name']}이고 {person['age']}살입니다.")

#4.
fruits = ["사과", "바나나", "딸기", "포도"]
for i, fruit in enumerate(fruits):
    print(i, fruit)

#5.
person = {"name": "다윗", "age": 28}
person["hobby"] = "코딩"
person["age"] = 29

print(person)

#6.
numbers = [1, 2, 3, 4, 5, 6, 7]

print(numbers[-3:])

#7.
words = ["사과", "수박", "파인애플", "딸기"]
longest = ""

for word in words:
    if len(word) > len(longest):
        longest = word
print(longest)

#8.
person = {"name": "다윗", "age": 28, "city": "서울"}

for key in person:
    print(key, ":", person[key])

   
#9.
a = ["사과", "바나나"]
b = ["딸기", "포도"]

print(a + b)

#10.
students = [
    {"name": "다윗", "score": 95},
    {"name": "철수", "score": 70},
    {"name": "영희", "score": 85},
]

for student in students:
    if student['score'] >= 80:
        print(f"{student['name']} {student['score']}점")
        
#11.
numbers = [1, 2, 2, 3, 3, 3, 4]

print(set(numbers))

#12.
person = {"name": "다윗", "age": 28, "city": "서울"}

for key in person:
    print(person[key])
    
#13.
fruits = ["사과", "바나나", "딸기", "포도"]


if  "딸기" in fruits :
    print("있어요!")
else:
    print("없어요!")

#14.
person = {}

person['name'] = "다윗"
person['age'] = 28
person['city'] = "서울"

print(person)

#15.
numbers = [10, 20, 30, 40, 50, 60]

print(numbers[::2])

#16.
numbers = [1, 2, 3, 4, 5]

print(numbers[::-1])

#17.
people = [
    {"name": "다윗", "age": 28},
    {"name": "철수", "age": 35},
    {"name": "영희", "age": 22},
]
oldest = people[0]#가정을 해놓는거(첫번째 사람이 일단 제일 나이 많다고 가정)

for person in people:
    if person["age"] > oldest["age"]:
        oldest = person
print(oldest["name"])

        
#18.
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

print(sorted(set(numbers)))

#19.
person = {"name": "다윗", "age": 28, "city": "서울"}

print(list(person.keys()))
    
#20.
fruits = ["사과", "바나나", "파인애플"]

result = {}
for i in fruits:
    result[i] = len(i)
print(result)
    