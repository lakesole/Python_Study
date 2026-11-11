numbers = [i * 2 for i in range(1, 6)]
print(numbers)

names = ["다윗", "철수", "다윗", "영희", "철수", "민준"]

name = set(names)
print(name)


numbers = [i for i in range(1, 11) if i % 3 == 0]
print(numbers)



students = {
    "다윗": {"age": 28, "score": 95},
    "철수": {"age": 25, "score": 88},
}

print(students["다윗"]['score'])
print(students["철수"]['age'])