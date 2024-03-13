def self_number(number):
    total_num = number
    while number != 0:
        total_num += number % 10
        number //= 10
    return total_num

self_numbers = set(range(1, 10001))
generated_numbers = set()

for i in range(1, 10001):
    generated_numbers.add(self_number(i))

self_numbers = self_numbers - generated_numbers

for num in sorted(self_numbers):
    print(num)