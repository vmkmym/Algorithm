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
# 인덱스의 몫과 나머지로 n x n 배열의 행과 열을 알 수 있습니다. 그 중 큰 값에 1을 더하면 배열의 값입니다.