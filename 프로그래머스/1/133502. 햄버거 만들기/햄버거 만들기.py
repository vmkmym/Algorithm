# 인덱스를 이용한 풀이
def solution(ingredient):
    burger = 0
    i = 0
    while i < len(ingredient) - 3:
        if ingredient[i:i+4] == [1, 2, 3, 1]:
            burger += 1
            del ingredient[i:i+4]
            i = max(0, i-4)
        else: 
            i += 1
    return burger

# 다른 사람 풀이
def solution(ingredient):
    stack = []
    burger = 0
    for i in ingredient:
        stack.append(i)
        if stack[-4:] == [1, 2, 3, 1]:
            burger += 1
            # del이나 clear, slice를 사용하지 않고 pop을 사용하여 효율적으로 제거
            # 처음에 이 풀이를 생각했는데, pop으로 안지워서 시간초과 발생했음
            for i in range(4):
                stack.pop()
    return burger

# 다른 사람 풀이 -> 제일 잘 푼 듯
def solution(ingredient):
    s = []
    answer = 0
    for i in ingredient:
        s.append(i)
        while s[-4:] == [1, 2, 3, 1]:
            s.pop()
            s.pop()
            s.pop()
            s.pop()
            answer += 1
    return answer