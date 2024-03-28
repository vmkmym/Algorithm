'''
    # 0: 청소 안한 곳, 1: 벽, 2: 청소한 곳
    1. 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
    2. if 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우,
        2-1. 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
        2-2. 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
    3. else 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우,
        1. 반시계 방향으로 90도 회전한다.   
        2. if 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 
            2-1. 한 칸 전진한다.
    3. 1번으로 돌아간다.
'''

# 현재 칸이 0이면 청소한다 room[x][y] = 2

# 현재 칸 주변에 청소할 빈 칸이 없는 경우
    # 후진할 수 있는지 확인
        # 후진할 수 있다면 후진
    # 후진할 수 없는 경우
        # 작동을 멈춤

# 현재 칸 주변에 청소할 빈 칸이 있는 경우
    # (for문) 반시계 방향으로 90도 회전 for _ in range(3)
    # if 칸이 청소할 빈 칸인지 확인
        # 청소할 빈 칸이라면 전진
            # 청소한 칸의 수를 세는 변수에 1을 더함
        # 청소할 빈 칸이 아니라면 1번으로 돌아감
# return cnt

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
            cnt += clean_room(nx, ny, d, room)  # 청소한 칸의 수를 더함
            return cnt  # 청소한 칸의 수를 반환

    # 모든 방향을 확인한 후에 후진하거나 작동을 멈추는 코드
    nx = x - dx[d]
    ny = y - dy[d]
    if room[nx][ny] == 1:
        return cnt  # 청소한 칸의 수를 반환
    else:
        return clean_room(nx, ny, d, room)  # 후진하지만 카운트는 증가시키지 않음

print(clean_room(x, y, d, room))