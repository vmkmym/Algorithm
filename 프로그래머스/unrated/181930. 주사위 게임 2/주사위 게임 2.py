def solution(a, b, c):
    unique = {a, b, c}
    count = len(unique)

    if count == 3:
        return a + b + c
    elif count == 2:
        return (a + b + c) * (a**2 + b**2 + c**2)
    else:
        return (a + b + c) * (a**2 + b**2 + c**2) * (a**3 + b**3 + c**3)

# 다른 사람의 풀이가 괜찮은게 딱히 없었음
