def solution(num_list):
    result = 1
    for num in num_list:
        result *= num
    return 1 if result < sum(num_list) **2 else 0