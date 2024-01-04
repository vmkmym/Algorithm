def solution(arr, k):
    unique_arr = []
    for num in arr:
        if num not in unique_arr:
            unique_arr.append(num)
    
    if len(unique_arr) < k:
        return unique_arr + [-1] * (k - len(unique_arr))
    else:
        return unique_arr[:k]