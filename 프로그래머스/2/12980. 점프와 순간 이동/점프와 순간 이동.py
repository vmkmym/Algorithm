def solution(n):
    count = 0
    while n != 0:
        if n % 2 == 0:
            n //= 2
        else:
            n -= 1
            count += 1 
    return count

# 다른 사람 풀이
def solution(n):
    return bin(n).count('1')
