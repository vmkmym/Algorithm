def solution(A, B):
    sorted_A = sorted(A)
    sorted_B = sorted(B, reverse=True)
    total = sum([x * y for x, y in zip(sorted_A, sorted_B)])
    return total