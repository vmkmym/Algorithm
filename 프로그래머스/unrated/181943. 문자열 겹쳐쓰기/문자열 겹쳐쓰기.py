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