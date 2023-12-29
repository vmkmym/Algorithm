def solution(array):
    return sum(str(i).count('7') for i in array)

# 다른 사람 풀이
def solution(array):
    return str(array).count('7')

def solution(array):
    return ''.join(map(str, array)).count('7')