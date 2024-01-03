from collections import deque

def solution(n_str):
    queue = deque(n_str)

    while queue and queue[0] == '0':
        queue.popleft()

    return ''.join(queue) if queue else '0'