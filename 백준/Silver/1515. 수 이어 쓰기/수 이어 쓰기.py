n = input()
number = 0
idx = 0

while True:
    number += 1
    for num in str(number):
        if n[idx] == num:
            idx += 1
            if idx >= len(n):
                print(number)
                break
    else:
        continue
    break