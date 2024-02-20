def solution(ingredient):
    burger = 0
    stack = []
    for i in ingredient:
        stack.append(i)
        if stack[-4:] == [1, 2, 3, 1]:
            burger += 1
            stack = stack[:-4]
    return burger

# 5, 12번 시간초과