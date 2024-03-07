def solution(n):
    # 2차원 배열 (행, 열)
    # dx, dy = (1, 0) 아래 (0, 1) 오른쪽 (-1, -1) 위
    dx = [1, 0, -1]
    dy = [0, 1, -1]
    b = [[0]*i for i in range(1, n+1)]
    x, y = -1, 0 # 현재 위치
    num = 1 # 숫자 1부터 시작해서 n까지 배열에 넣어야 함.
    
    for i in range(n):
        for j in range(i, n):
            x += dx[i%3]
            y += dy[i%3]
            b[x][y] = num
            num += 1
            
    return sum(b, [])