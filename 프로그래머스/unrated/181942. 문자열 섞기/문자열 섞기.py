def solution(str1, str2):
    answer = ''.join(i + j for i, j in zip(str1, str2))
    return answer

# 다른 사람의 풀이
def solution(str1, str2):
    answer = ''.join([str1[i] + str2[i] for i in range(len(str1))])
    return answer
