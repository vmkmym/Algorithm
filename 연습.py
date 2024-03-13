def self_number(number):
    total_num = number
    while number != 0:
        total_num += number % 10
        number //= 10
    return total_num

self_numbers = {num for num in range(1, 10001) if self_number(num) not in range(1, 10001)}

for num in sorted(self_numbers):
    print(num)