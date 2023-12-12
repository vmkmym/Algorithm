def solution(n):
    answer = 0
    if n % 2 == 1:
        for i in range(1, n + 1):
            if i % 2 == 1:
                answer += i
    else:
        for i in range(1, n + 1):
            if i % 2 == 0:
                answer += i * i
    return answer  

# 다른 고수의 풀이, 이해가 잘 안감
def solution(n):
    return sum(x ** (2 - x % 2) for x in range(n + 1) if n % 2 == x % 2)

# 이거는 이해가 감 range(시작값, 마지막값, 간격)
def solution(n):
    if n%2:
        return sum(range(1,n+1,2))
    return sum([i*i for i in range(2,n+1,2)])
