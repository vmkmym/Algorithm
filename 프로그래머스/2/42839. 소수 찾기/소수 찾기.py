from itertools import permutations

def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

def solution(numbers):
    unique_numbers = set() 
    for length in range(1, len(numbers) + 1): 
        perm = permutations(numbers, length) 
        for i in list(perm): # 순열을 튜플로 반환하므로 리스트로 변환
            num = int(''.join(i)) # 튜플을 문자열로 변환 후 정수로 변환
            unique_numbers.add(num) # 중복된 수를 제거하기 위해 set에 추가

    prime_count = 0
    for num in unique_numbers:
        if is_prime(num):
            prime_count += 1

    return prime_count