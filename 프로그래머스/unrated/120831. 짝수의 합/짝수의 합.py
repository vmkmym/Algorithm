def solution(n):
    return sum(even for even in range(1, n + 1) if even % 2 == 0)