def solution(a, b, c, d):
    dice = [a, b, c, d]
    dice.sort()

    if len(set(dice)) == 1: # 모두 같은 숫자인 경우
        return 1111 * dice[0]
    
    elif len(set(dice)) == 2:
        counts = [dice.count(x) for x in set(dice)] # 각 숫자 count
        if 3 in counts:
            p = list(set(dice))[counts.index(3)] # 3번 나온 숫자 할당
            q = list(set(dice))[counts.index(1)] # 1번 나온 숫자 할당
            return (10 * p + q) ** 2
        else:
            p, q = list(set(dice)) # 2번 나온 숫자 각각 할당
            return (p + q) * abs(p - q)
        
    elif len(set(dice)) == 3:
        for x in set(dice): 
            if dice.count(x) == 2: # 2번 count한 숫자 p에 저장하고
                p = x
                rest = [y for y in set(dice) if y != p] # 아닌 숫자를 list에 저장
                return rest[0] * rest[1]
    else:
        return dice[0]

# 이건 도저히 혼자선 테스트 케이스를 다 통과하지 못했음
# gpt와 1시간 대화하다가 얻어낸 코드_7점 받음
        
### 정렬을 왜 할까?
# 정렬된 숫자는 같은 숫자끼리 묶여있어 해당 문제를 해결하는 데 있어서 코드의 가독성과 효율성을 높임
# 주사위의 숫자들을 일관된 순서로 배열하여, 조건을 판단하기 쉽게 하기 위함

# 그 외의 배운 점은 나중에 정리할 예정..
