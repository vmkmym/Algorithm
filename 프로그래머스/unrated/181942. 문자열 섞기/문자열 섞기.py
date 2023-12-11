def solution(str1, str2):
    answer = ''.join(i + j for i, j in zip(str1, str2))
    return answer