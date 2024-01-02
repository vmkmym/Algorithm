def solution(num_list):
    return [sum(1 for even in num_list if even % 2 == 0), sum(1 for odd in num_list if odd % 2 != 0)]
