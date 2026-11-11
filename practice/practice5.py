#1.
def add(a, b):
    return(a + b)

print(add(3, 5))
print(add(10, 20))

#2.
def greet(name):
    return(f"안녕하세요, {name}님!")

print(greet("다윗"))
print(greet("철수"))

#3.
def is_even(a):
    if a % 2 == 0:
        return True
    elif a % 2 == 1:
        return False

print(is_even(4))
print(is_even(7))

#4.

def total(numbers):
    box = 0
    for i in numbers:
        box = box + i
    return(box)

print(total([1, 2, 3, 4, 5]))
print(total([10, 20, 30]))    

#5.
def bigger(a, b):
    if a > b:
        return a
    else:
        return b

print(bigger(3, 7))
print(bigger(10, 4)) 

#6.
def find_max(numbers):
    max = 0
    for number in numbers:
        if number >= max:
            max = number
    return max

print(find_max([3, 1, 7, 2, 9, 4]))
print(find_max([10, 50, 20, 40]))

#7.
def count_chars(text):
    return len(text)

print(count_chars("안녕하세요"))
print(count_chars("python"))

#8.
def check_age(name, age):
    if age >= 18:
        return(f"{name}님은 성인입니다.")
    else:
        return(f"{name}님은 미성년자입니다.")
    
print(check_age("다윗", 28))
print(check_age("철수", 15))

#9.
def get_evens(numbers):
    number = []
    for i in numbers:
        if i % 2 == 0:
            number.append(i)
    return(number)

print(get_evens([1, 2, 3, 4, 5, 6, 7, 8]))

#10.
def is_multiple(a, b):
    if a % b == 0:
        return True
    else:
        return False
    
print(is_multiple(10, 5))
print(is_multiple(10, 3))

#11.
def sum_to(a):
    total = 0
    for i in range(1 , a + 1):
        total = total + i
    return(total)

print(sum_to(5))
print(sum_to(10))   


#12.
def reverse(word):
    return(f"{word[::-1]}")

print(reverse("안녕하세요"))
print(reverse("python"))

#13. 
def calc(a, b):
    return a * b, a / b

mul, div = calc(10, 2)
print(mul)
print(div)



#14.
def welcome_all(name):
    for i in name:
        print(f"{i}님 환영합니다!")

welcome_all(["다윗", "철수", "영희"])

#15.
def average(number):
    ave = 0
    for i in number:
        ave = ave + i
    return (ave) / len(number)

print(average([10, 20, 30, 40, 50]))
print(average([1, 2, 3]))

#16.
def to_upper(word):
    return(word.upper())
    

print(to_upper("hello"))
print(to_upper("python"))

#17.
def find_min(numbers):
    min_num = numbers[0]
    for number in numbers:
        if min_num >= number:
            min_num = number
    return(min_num)

print(find_min([3, 1, 7, 2, 9, 4]))
print(find_min([10, 50, 20, 40]))

#18.
def pass_check(name, score):
    if score >= 60:
        return(f"{name}님 합격!")
    else:
        return(f"{name}님 불합격!")
    
print(pass_check("다윗", 85))
print(pass_check("철수", 45))

#19.
def gugudan(a):
    for i in range(1, 10):
        print(f"{a} X {i} = {a * i}")
            
gugudan(3)

#20.
def common(a, b):
    word = []
    for i in a:
        if i in b:
            word.append(i)
    return(word)

print(common([1, 2, 3, 4], [3, 4, 5, 6]))
        