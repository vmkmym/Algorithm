def solution(ingredient):
    burger = 0
    i = 0
    while i < len(ingredient) - 3:
        if ingredient[i:i+4] == [1, 2, 3, 1]:
            burger += 1
            del ingredient[i:i+4]
            i = max(0, i-4)  # 인덱스 값을 감소시킵니다.
        else:
            i += 1
    return burger