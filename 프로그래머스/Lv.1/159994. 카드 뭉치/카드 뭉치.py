def solution(cards1, cards2, goal):
    i, j, k = 0, 0, 0
    while k < len(goal):
        if i < len(cards1) and cards1[i] == goal[k]:
            i += 1
        elif j < len(cards2) and cards2[j] == goal[k]:
            j += 1
        else:
            return "No"
        k += 1
    return "Yes"

# 투 포인터 알고리즘은 배열이나 리스트와 같은 선형 자료구조를 순회할 때 사용하는 효율적인 방법입니다. 
# 이 알고리즘은 이름에서 알 수 있듯이 두 개의 포인터를 사용합니다. 
# 이 두 포인터는 보통 시작점과 끝점을 가리키거나, 같은 위치에서 시작해 서로 다른 방향으로 이동합니다.