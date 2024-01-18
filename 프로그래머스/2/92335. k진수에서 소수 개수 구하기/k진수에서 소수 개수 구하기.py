def solution(n, k):
    # 주어진 숫자를 k진수로 변환
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    # n을 k진수로 변환
    converted = ''
    while n > 0:
        n, mod = divmod(n, k) # 몫, 나머지
        converted = str(mod) + converted # 나머지를 앞에 붙임
        print(n, mod, converted)
        
    # k진수로 변환된 숫자를 0을 기준으로 split
    candidates = converted.split('0')

    # 소수 판별
    count = 0
    for candidate in candidates:
        if candidate and is_prime(int(candidate)):
            count += 1

    return count

# 다른 사람의 풀이 : 엄청 간단하다.
def conv(n, k):
    s = ''
    while n:
        s += str(n%k)
        n //= k
    return s[::-1]