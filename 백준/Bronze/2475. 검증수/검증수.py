numbers = map(int, input().split())
def remainder(numbers):
    sum = 0
    for number in numbers:
        sum += number ** 2
    return sum % 10
print(remainder(numbers))