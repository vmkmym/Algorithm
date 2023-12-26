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
# gpt와 1시간 대화하다가 얻어낸 코드 _ 7점 받음
        
### 정렬을 왜 할까?
    # 정렬된 숫자는 같은 숫자끼리 묶여있어 해당 문제를 해결하는 데 있어서 코드의 가독성과 효율성을 높임
    # 주사위의 숫자들을 일관된 순서로 배열하여, 조건을 판단하기 쉽게 하기 위함

### 피드백 이후 새롭게 공부한 내용 (출처 codesyun.tistory.com 인데 여기선 [이것이 코딩테스트다 with 파이썬] 보고 작성했다고 함)

# 다이나믹 프로그래밍 Dynamic Programming
    # 큰 문제를 작은 문제로 나누어 해결하는 방법이며, 작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일
    # 피보나치 함수는 Bottom-Up 방식으로 작은 문제부터 답을 도출하며 반복문 이용하는 전형적인 형태이다

# 메모이제이션 Memoization
    # DP를 구현하는 방법 중 한 종류
    # 한 번 구한 결과를 메모리 공간에 메모해두고 같은 식을 다시 호출하면 메모한 결과를 그대로 가져오는 기법
    # 값을 저장하는 방법이라서 캐싱 Cashing 이라고 한다
