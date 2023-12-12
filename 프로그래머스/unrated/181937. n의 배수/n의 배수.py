def solution(num, n):
    if 2 <= num <= 100 and 2 <= n <= 9:
        return 1 if num % n == 0 else 0
