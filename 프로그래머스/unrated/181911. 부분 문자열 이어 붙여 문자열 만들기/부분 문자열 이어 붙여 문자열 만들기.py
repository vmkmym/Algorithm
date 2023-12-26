def solution(my_strings, parts):
    result = []
    
    for my_str, part in zip(my_strings, parts):
        s, e = part
        result.append(my_str[s:e + 1])

    return ''.join(result)
    
# 다른 사람 풀이는 대체로 비슷하고 지금 이 코드를 한 줄 코딩한 풀이가 많았음
# zip을 활용할 수 있는 좋은 예제
