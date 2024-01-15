def solution(n, m, section):
    paint_count = 1 # 최소한 한번은 칠해야 하므로 1로 초기화
    start = section[0] # 칠할 수 있는 범위의 시작점을 초기화

    for i in section: 
        if i - start >= m: # 칠할 수 있는 범위를 넘어가면
            start = i # 시작점을 현재 위치로 초기화
            paint_count += 1

    return paint_count
