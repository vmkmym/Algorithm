from bisect import bisect_right

def solution(A, B):
    B.sort()
    count = 0
    for a in A:
        index = bisect_right(B, a) # a보다 큰 값이 처음 나오는 인덱스, 없으면 len(B)
        if index < len(B):
            del B[index]
            count += 1
        else: # a보다 큰 값이 없으면 가장 작은 값을 제거
            del B[0]
    return count