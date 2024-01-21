def solution(land):
    for i in range(1, len(land)):
        for j in range(4):
            max_value = max(land[i-1][:j] + land[i-1][j+1:])
            land[i][j] += max_value
    return max(land[-1])