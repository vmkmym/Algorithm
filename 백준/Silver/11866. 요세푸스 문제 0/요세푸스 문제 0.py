from collections import deque

N, K = map(int, input().split())
queue = deque(range(1, N+1))
result = []

while queue:
    queue.rotate(-K) # 왼쪽으로 k번 이동
    result.append(queue.pop()) # K번째 요소를 pop하여 result에 추가
    
print("<" + ", ".join(map(str, result)) + ">")