#Quiz 1
import random

def random_lotto():
    result = []
    while len(result) < 6:
            num = random.randint(1,45)
            if num not in result:
                result.append(num)
    return result
print(random_lotto())


#Quiz 2
class Gugu:
    def __init__(self, num):
        self.num = num

    def output(self):
        for i in range(1,10):
            print(f"{self.num} X {i} = {self.num * i}")

#Quiz 2 출력
five_dan = Gugu(5)
five_dan.output()

