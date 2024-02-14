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

# 다른 사람의 풀이
# 시간 복잡도는 O(n*m)
# board의 모든 행과 열을 순회함 O(n*n)
# moves의 모든 원소를 순회함 O(m)
# 이 두 부분은 독립적으로 수행되므로, 전체 시간 복잡도는 두 부분의 시간 복잡도의 합, 즉 O(nn + m)이 됩니다. 하지만 보통 시간 복잡도에서는 가장 큰 항만을 고려하므로, 이 코드의 시간 복잡도는 O(nm)으로 볼 수 있습니다.
def solution(board, moves):
    # board를 전치(transpose)한 후 0을 제거하여 각 열을 리스트로 만든 것
    cols = [list(filter(lambda y: y > 0, x)) for x in zip(*board)]
    # a는 터트려진 인형의 개수, s는 뽑힌 인형을 저장하는 스택
    a, s = 0, [0]

    for m in moves:
        if cols[m - 1]:
            # 뽑은 인형 d와 스택의 가장 위의 인형 l을 비교하여 같으면 터트리고
            if (d := cols[m - 1].pop(0)) == (l := s.pop()):
                a += 2
            # 같지 않으면 스택에 다시 넣는다
            else:
                s.extend([l, d])
    return a