def solution(arr, idx):
    if 1 not in arr[idx:]:
        return -1
    
    for i in range(idx, len(arr)):
        if arr[i] == 1:
            return i
