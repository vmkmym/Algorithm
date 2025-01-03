n = int(input())
digits = list(map(int, input().strip()))
total_sum = 0
for i in range(n):
    total_sum += digits[i]
print(total_sum)