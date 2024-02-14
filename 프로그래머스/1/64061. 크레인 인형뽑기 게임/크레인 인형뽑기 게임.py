def solution(board, moves):
    basket = []
    doll_count = 0
    top = [0] * len(board) # 가장 위에 있는 인형의 위치 저장할 리스트
    
    for i in range(len(board)): 
        for j in range(len(board)):
            if board[j][i] != 0: 
                top[i] = j # 인형이 있으면 top에 위치 저장 해놓고
                break
    
    for move in moves: # 크레인의 위치 순회
        if top[move - 1] < len(board): # top[move - 1]은 move번째 크레인의 위치, 1부터 시작하므로 -1
            basket.append(board[top[move - 1]][move - 1]) # board에 있는 인형을 basket에 넣음
            top[move - 1] += 1 # top에 있는 위치를 한칸 내림 이렇게 하면 다음에 같은 위치에 있는 인형을 가져올 수 있음
            
            if len(basket) > 1 and basket[-1] == basket[-2]: # 같은 인형이면
                basket.pop(-1) # 같은 인형 두 개 제거
                basket.pop(-1)
                doll_count += 2
                
    return doll_count

# 시간복잡도 O(n+m)