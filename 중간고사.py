def odd_or_even(num):
    if num % 2 == 0:
        return "짝수"
    else:
        return "홀수"

result = odd_or_even(2)
print("답:", result)