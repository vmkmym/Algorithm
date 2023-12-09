def solution(my_string, overwrite_string, s):
    answer = ''
    i = 0
    while i < len(my_string):
        if i == s:
            answer += overwrite_string
            i += len(overwrite_string)
        else:
            answer += my_string[i]
            i += 1
    return answer

# 나는 조건문, 반복문 썼는데 안쓰고 간단하게 하는 방법
answer = my_string[:s] + overwrite_string + my_string[ s + len(overwrite_string): ]
