#1
a = input("문자를 입력해주세요.: ")

if a == "안녕하세요.":
    print("반갑습니다.")
else:
    print("인사를 먼저하세요.")

#2
numbers = int(input("값을 입력하세요.:"))
a = numbers + 100

if a >= 150:
    print(a)
elif a <= 150:
    print("값이 부족합니다.")

#3
numbers = [100, 200, 300]
result = []

for i in numbers:
    price = i * 1.1
    result.append(int(price))

print(result)

#4
numbers = [3, 100, 23, 33, 72, 94]
result = []


for i in numbers:
    if i % 3 == 0:
        result.append(numbers)

print(result)

#5
b = 1

while b <= 1000:
    print(b)
    b = b + 1

#6
c = 0
d = 0

while c <= 100 :
    if c % 2 != 0 :
        d += c
    c = c + 1

print(f"1~100 중 홀수의 합 : {d}")



