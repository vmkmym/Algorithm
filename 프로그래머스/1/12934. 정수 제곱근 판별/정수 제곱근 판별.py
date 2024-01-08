import math

def solution(n):
    if math.sqrt(n) == int(math.sqrt(n)):
        return (int(math.sqrt(n)) + 1) ** 2
    else:
        return -1

# 일반적인 방법으로 로직을 짜게 되면 시간복잡도가 너무 높아짐
# 제한된 범위에서 효율적인 알고리즘을 설계하기 위해서는 주어진 조건을 최대한 활용하고, 문제를 간소화하여 해결 방안을 찾아야함