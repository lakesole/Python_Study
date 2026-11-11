#1.
point = (10, 20, 30, 40, 50)

print(point[0], point[-1])

#2.
numbers = [1, 2, 2, 3, 3, 3, 4, 4]

unique = set(numbers)
to_list = list(unique)

print(to_list)

#3.
numbers = [i * i for i in range(1, 11)]
print(numbers)

#4. 
numbers = [i for i in range(1, 21) if i % 5 == 0]
print(numbers)

#5.
a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}

print(a & b)

#6.
numbers = [3, 15, 7, 22, 8, 11, 4, 19]

numbers = [i for i in numbers if i > 10]
print(numbers)

#7.
a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)

#8.
words = ["hello", "python", "world"]

word = [i.upper() for i in words ]
print(word)

#9.
t = (1, 2, 3)
l = [4, 5, 6]

print(list(t))
print(tuple(l))

#10.
words = ["사과", "수박", "파인애플", "키위", "블루베리"]
word = [i for i in words if len(i) >= 3]
print(word)

#11.
number = [i for i in range(1, 11) if i % 2 == 1]
print(number)

#12.
numbers = [1, 2, 2, 3, 3, 3, 4]
number = set(numbers)

total = len(numbers) - len(number)

print(f"중복된 값: {total}개")

#13.
a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}

print(a - b)

#14.
numbers = [1, 2, 3, 4, 5]

answer = [i + 10 for i in numbers]
print(answer)

#15.
numbers = (3, 1, 7, 2, 9, 4)
print(max(numbers))

#16.
numbers = [1, 2, 3, 4, 5, 6]
number = [i * i for i in numbers if i % 2 == 0]
print(number)

#17.
words = ["apple", "banana", "cherry", "avocado", "grape"]
word = [i for i in words if "a" in i]
print(word)

#18.
a = [1, 2, 3, 4, 5]
b = [3, 4, 5, 6, 7]

print(set(a) & set(b))

#19.
words = ["사과", "바나나", "파인애플"]
word = [len(i) for i in words ]
print(word)

#20.
numbers = [1, 2, 2, 3, 3, 3, 4]
unique = set(numbers)
total = 0
for i in unique:
    total = total + i
print(total)