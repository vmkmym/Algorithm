def solution(dots):
    return (max(dots)[0]-min(dots)[0]) * (max(dots)[1]-min(dots)[1])

# 뭐지 다른 사람 풀이 맨 위가 내 풀이라니!
# return max(dots)[0]-min(dots)[0] * max(dots)[1]-min(dots)[1]
    # 처음에 이렇게 풀었는데 안되서 뭐가 문제지 하다가 괄호하니까 통과

# 다른 사람 풀이
def solution(dots):
    dots.sort()

    x_min, y_min = dots[0]
    x_max, y_max = dots[-1]

    return (x_max-x_min) * (y_max-y_min)
