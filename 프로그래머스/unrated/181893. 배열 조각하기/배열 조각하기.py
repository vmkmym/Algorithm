def solution(arr, query):
    for i, e in enumerate(query):
        if i % 2 == 0:
            arr = [arr[j] for j in range(len(arr)) if j <= e]
        else:
            arr = [arr[j] for j in range(len(arr)) if j >= e]
    return arr

