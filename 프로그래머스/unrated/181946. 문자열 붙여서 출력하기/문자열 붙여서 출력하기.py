str1, str2 = input().strip().split(' ')
if 1 <= len(str1) <= 10 and 1 <= len(str2) <= 10:
    output = str1 + str2
    print(output)

# 이렇게 공백을 줄이면 한 줄로 끝남
print(input().strip().replace(' ', ''))
