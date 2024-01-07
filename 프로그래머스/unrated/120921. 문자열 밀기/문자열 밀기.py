from collections import deque

def solution(A, B):
    if len(A) != len(B):
        return -1

    rotated = deque(A)

    for count in range(len(A)):
        if ''.join(rotated) == B:
            return count
        rotated.rotate(1)

    return -1

# deque 겨냥 문제인가