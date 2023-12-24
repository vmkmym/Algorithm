def solution(arr, queries):
    result = []
    for s, e, k in queries:
        value = [i for i in arr[s:e+1] if i > k]
        if value:
            result.append(min(value))
        else:
            result.append(-1)
    return result

# s, e, k로 쓰고 싶었음
# value에 리스트 컴프리헨션 이용하니까 코드가 간결해진다
