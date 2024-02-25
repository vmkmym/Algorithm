def solution(friends, gifts):
    # 친구들의 이름을 인덱스로 변환한 딕셔너리
    friend_to_index = {friend: index for index, friend in enumerate(friends)}
    n = len(friends)

    # 친구들끼리 주고 받은 선물을 저장할 2차원 리스트
    gift_counts = [[0]*n for _ in range(n)]

    # 2차원 리스트에 주고 받은 선물을 저장
    for gift in gifts:
        giver, receiver = gift.split()
        i, j = friend_to_index[giver], friend_to_index[receiver]
        gift_counts[i][j] += 1

    # 다음 달에 줄 선물의 개수를 저장할 리스트
    gifts_next_month = [0]*n
    
    # 다음 달에 줄 선물의 개수를 계산 
    # 1. i가 j에게 준 선물이 j가 i에게 준 선물보다 많을 때
    # 2. i가 j에게 준 선물과 j가 i에게 준 선물이 같을 때
    # 3. i가 받은 선물의 합이 j가 받은 선물의 합보다 많을 때
    for i in range(n):
        for j in range(n):
            if i != j: # 자기 자신에게 선물을 주는 경우를 제외하고
                if (gift_counts[i][j] > gift_counts[j][i] or # i가 j에게 준 선물이 j가 i에게 준 선물보다 많을 때
                        (gift_counts[i][j] == gift_counts[j][i] and # i가 j에게 준 선물과 j가 i에게 준 선물이 같을 때
                         sum(gift_counts[i]) - sum(row[i] for row in gift_counts) > sum(gift_counts[j]) - sum(row[j] for row in gift_counts))): # i가 받은 선물이 j가 받은 선물보다 많을 때
                    gifts_next_month[i] += 1 # 다음 달에 i는 선물을 받음
                    
    return max(gifts_next_month)