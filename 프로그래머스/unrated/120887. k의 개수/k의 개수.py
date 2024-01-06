def solution(i, j, k):
    count = 0
    for e in range(i, j+1):
        count += str(e).count(str(k))
    return count