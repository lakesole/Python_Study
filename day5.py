fruits = ["사과", "바나나", "딸기"]

print(fruits[0])   # 사과
print(fruits[1])   # 바나나
print(fruits[2])   # 딸기
print(fruits[-1]) 

numbers = [0, 1, 2, 3, 4, 5]

print(numbers[1:4])
print(numbers[:3])
print(numbers[3:])


fruits = ["사과", "바나나"]

fruits.append("딸기")
fruits.remove("바나나")
fruits.pop()
len(fruits)

person = {
    "name": "다윗",
    "age" : 28,
    "job" : "개발자"
}

print(person["name"])
print(person["age"])

person = {"name": "다윗", "age": 28}

person["job"] = "개발자"
person["age"] = 29
del person["job"]

print(person)

person = {"name": "다윗", "age": 28, "job": "개발자"}

for key in person:
    print(key, ":", person[key])
    



#문제 
# 1. 
numbers = [1, 2, 3, 4, 5, 6, 7]

print(numbers[2:5])

# 2.
fruits = ["사과", "바나나", "딸기"]

fruits.append("포도")
fruits.remove("바나나")

print(fruits)

# 3.
person = {"name": "다윗", "age": 28, "city": "서울"}

print(f"저는 {person['name']}이고 {person['age']}살입니다.")

# 4.
person = {"name": "다윗", "age": 28}

person ["hobby"] = "코딩"
person ["age"] = 29

print(person)

