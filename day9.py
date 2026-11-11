import math

print(math.pi)
print(math.sqrt(16))
print(math.ceil(3.2))
print(math.floor(3.8))


from math import sqrt
sqrt(16)

import math as m
m.sqrt(16)

import random
random.random()
random.randint(1, 10)
random.choice(["가위", "바위", "보"])
random.shuffle([1, 2, 3, 4, 5])

from datetime import datetime
now = datetime.now()
print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.strftime("%Y-%m-%d"))

import os
print(os.getcwd())
print(os.listdir("."))
os.mkdir("new_folder")

#문제
#1.
import math
print(math.sqrt(25))
print(round(math.pi, 3))

#2.
import random
numbers = []
for i in range(5):
    numbers.append(random.randint(1, 100))

print(numbers)

#3.
from datetime import datetime
now = datetime.now()
print(f"오늘은 {now.year}년 {now.month}월 {now.day}일입니다.")
