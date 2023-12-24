def solution(arr, queries):
    result = []
    for s, e, k in queries:
        value = [x for x in arr[s:e+1] if x > k]
        if value:
            result.append(min(value))
        else:
            result.append(-1)
    return result
