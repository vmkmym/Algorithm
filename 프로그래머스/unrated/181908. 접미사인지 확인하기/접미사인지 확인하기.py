def solution(my_string, is_suffix):
    suffixes = sorted([my_string[i:] for i in range(len(my_string))])
    return 1 if is_suffix in suffixes else 0
