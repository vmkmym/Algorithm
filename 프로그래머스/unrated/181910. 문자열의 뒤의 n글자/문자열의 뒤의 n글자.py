def solution(my_string, n):
    return my_string[-n:]

# 다른 풀이
solution = lambda my_string, n : my_string[len(my_string)-n:]
