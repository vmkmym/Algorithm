def solution(n, left, right):
    arr = []
    
    for i in range(left, right+1):
        row = i // n
        col = i % n
        num = max(row, col) + 1
        arr.append(num)
    
    return arr

# i가 속하는 행의 인덱스
# i가 속하는 열의 인덱스
# i가 속하는 행과 열 중에서 더 큰 값에 1을 더한 값