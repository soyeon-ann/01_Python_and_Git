#1
def add(a, b, c, d):
    result = a + b + c + d
    return result

sum_result = add(1, 2, 3, 4)
print("답:", sum_result)

def multiply(a, b, c, d):
    result = a * b * c * d
    return result

multiply_result = multiply(1, 2, 3, 4)
print("답:", multiply_result)

#2
def odd_or_even(num):
    if num % 2 == 0:
        return "짝수"
    else:
        return "홀수"

dis_result = odd_or_even(1)
print("답:", dis_result)

#3
def average(num):
    total = 0
    for i in num:
        total += i
    return total/len(num)

calculate_num = average([1,2,3,4,5])
print("답:", calculate_num)

#4
class GameCharacter:
    def __init__(self, id, gender, job):
        self.id = id
        self.gender = gender
        self.job = job

    def attack(self):
        print("공격!")

character = GameCharacter("player1", "여성", "마법사")
character.attack()

#5
class RealEstate:
    def __init__(self, location, size, building_type, price, year_built):
        self.location = location
        self.size = size
        self.building_type = building_type
        self.price = price
        self.year_built = year_built

    def display_info(self):
        print(f"위치: {self.location}")
        print(f"평수: {self.size}")
        print(f"건물 종류: {self.building_type}")
        print(f"가격: {self.price}")
        print(f"건축 연도: {self.year_built}")


estate = RealEstate("하남", 70, "아파트", 400000000, 2020)
estate.display_info()


