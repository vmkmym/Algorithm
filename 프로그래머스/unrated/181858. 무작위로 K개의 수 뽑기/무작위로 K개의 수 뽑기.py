def solution(arr, k):
    pick = []
    
    for i in arr:
        if i not in pick:
            pick.append(i)
        if len(pick) == k:
            break

    return pick + [-1] * (k - len(pick))