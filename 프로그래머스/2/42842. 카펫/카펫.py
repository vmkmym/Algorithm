def solution(brown, yellow):
    carpet = brown + yellow
    
    for x in range(1, int(carpet ** 0.5) + 1):
        if carpet % x == 0:
            y = carpet // x
            if (x-2) * (y-2) == yellow:
                return [max(x, y), min(x, y)]