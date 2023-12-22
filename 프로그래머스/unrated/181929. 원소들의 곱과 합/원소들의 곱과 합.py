def solution(num_list):
    result = 1
    for num in num_list:
        result *= num
    return 1 if result < sum(num_list) **2 else 0

# 다른 사람 풀이 중에서 모듈 가져와서 람다로 푸는게 있었음
