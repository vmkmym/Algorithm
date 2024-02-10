def solution(arr):
    answer = [0, 0]

    def check(size, x, y): # size: 한 변의 길이, x: 시작점 x좌표, y: 시작점 y좌표
        if size == 1: # 한 칸이면
            answer[arr[y][x]] += 1 # 해당 값에 1 더하고
            return
        else: # 한 칸이 아니면
            first_value = arr[y][x] # 첫 번째 값 저장
            for i in range(y, y+size): # 해당 범위만큼 반복
                for j in range(x, x+size): 
                    if arr[i][j] != first_value: # 첫 번째 값과 다르면
                        half = size // 2 # 반으로 나누고
                        check(half, x, y) # 4등분해서 다시 체크
                        check(half, x+half, y) 
                        check(half, x, y+half) 
                        check(half, x+half, y+half) 
                        return 
            answer[first_value] += 1 # 모두 같으면 해당 값에 1 더하고

    check(len(arr), 0, 0) 
    return answer