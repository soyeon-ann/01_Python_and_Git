#1
class user:
    def __init__(self,name,age,number):
       self.name = name
       self.age = age
       self.number = number

    def show(self):
        print(f"가입하신 계정의 이름은 {self.name}이며, 나이는 {self.age}, 그리고 연락처는 {self.number}입니다.")

gest = user("안소연",24, "010-3643-1111")
gest.show()

#2
def Length(talk):
    if len(talk) <= 20:
        return 50
    else:
        return 100

talk = input("문자 메시지를 입력하세요: ")
charge = Length(talk)
print(f"문자 요금은 {charge}원입니다.")