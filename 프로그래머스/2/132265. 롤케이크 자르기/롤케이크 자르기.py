from collections import Counter

def solution(topping):
    right = Counter(topping)
    left = Counter()

    count = 0
    for i in range(len(topping) - 1):
        left[topping[i]] += 1
        right[topping[i]] -= 1
        if right[topping[i]] == 0: # 토핑이 0개가 되면 삭제
            del right[topping[i]]
        if len(left) == len(right): # 왼쪽과 오른쪽의 토핑 종류가 같으면 카운트
            count += 1

    return count