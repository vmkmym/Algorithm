n, m = map(int, input().split())
x, y, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)] 

def turn_left(d): # 반시계 방향으로 90도 회전
    return (d - 1) % 4

def clean_room(x, y, d, room):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    room[x][y] = 2 # 청소한 경우는 2로 표시
    cnt = 1  # 무조건 처음엔 빈 칸이라 청소하니까
    for _ in range(4):
        d = turn_left(d)
        nx = x + dx[d] 
        ny = y + dy[d] 
        if room[nx][ny] == 0:
            cnt += clean_room(nx, ny, d, room) 
            return cnt  

    # 모든 방향을 확인한 후에 후진하거나 작동을 멈추는 코드
    nx = x - dx[d]
    ny = y - dy[d]
    if room[nx][ny] == 1:
        return cnt  
    else:
        return clean_room(nx, ny, d, room)  # 후진하지만 카운트는 증가시키지 않음

print(clean_room(x, y, d, room))