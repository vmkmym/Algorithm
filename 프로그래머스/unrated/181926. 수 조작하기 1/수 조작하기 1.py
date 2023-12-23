def solution(n, control):
    for i in control:
        if i == 'w':
            n += 1
        elif i == 's':
            n -= 1
        elif i == 'd':
            n += 10
        elif i == 'a':
            n -= 10
    return n

# 5점받았지만 더 짧게 쓰고 싶었음

# 딕셔너리, 리스트 컴프리헨션 사용하는 풀이
def solution(n, control):
    c = {'w': 1, 's': -1, 'd': 10, 'a': -10}
    return n + sum(c[i] for i in control)
