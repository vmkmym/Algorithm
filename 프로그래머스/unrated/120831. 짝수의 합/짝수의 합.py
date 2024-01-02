def solution(n):
    return sum(even for even in range(1, n + 1) if even % 2 == 0)

# 다른 사람 풀이
def solution(n):
    return sum(i for i in range(2, n + 1, 2))
