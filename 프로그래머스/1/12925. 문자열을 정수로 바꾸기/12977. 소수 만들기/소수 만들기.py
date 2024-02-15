from itertools import combinations

def solution(nums):
    combs = list(combinations(nums, 3))
    answer = 0
    for comb in combs:
        if is_prime(sum(comb)):
            answer += 1
    return answer

def is_prime(num):
    if num == 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num%i == 0:
            return False
    return True