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
