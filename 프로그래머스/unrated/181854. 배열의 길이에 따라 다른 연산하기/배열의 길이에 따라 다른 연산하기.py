def solution(arr, n):
    result = []
    
    for i in range(len(arr)):
        if len(arr) % 2 == 1 and i % 2 == 0:
            result.append(arr[i] + n)
        elif len(arr) % 2 == 0 and i % 2 == 1:
            result.append(arr[i] + n)
        else:
            result.append(arr[i])
            
    return result
