def solution(num, n, m):
    return int((num % n == 0) and (num % m == 0))

# 입력값 조건 추가 시
def solution(num, n, m):
    if not (2 <= n < 10 and 2 <= m < 10 and 10 <= num <= 100):
        return 0
    return int((num % n == 0) and (num % m == 0))
