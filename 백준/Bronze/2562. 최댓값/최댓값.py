numbers = [int(input()) for _ in range(9)]
max_number = -1
max_index = -1
for i in range(9):
    if numbers[i] > max_number:
        max_number = numbers[i]
        max_index = i + 1
        
print(max_number)
print(max_index)