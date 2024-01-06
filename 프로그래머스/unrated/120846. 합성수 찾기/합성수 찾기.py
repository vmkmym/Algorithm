def solution(n):
    count = 0

    for i in range(1, n + 1):
        divisors = sum(1 for j in range(1, i + 1) if i % j == 0)
        if divisors >= 3:
            count += 1

    return count
