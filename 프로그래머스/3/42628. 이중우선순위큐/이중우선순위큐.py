def solution(operations):
    queue = []
    for operation in operations:
        op, num = operation.split()
        if op == 'I':
            queue.append(int(num))
        elif queue:
            if num == '1':
                queue.remove(max(queue))
            else:
                queue.remove(min(queue))
    return [0, 0] if not queue else [max(queue), min(queue)]

# 이중우선순위큐를 이용한 풀이
'''
이 코드는 최소 힙과 최대 힙 두 개를 사용하여 이중 우선순위 큐를 구현합니다. 
숫자를 삽입할 때는 두 힙에 모두 삽입하고, 
최대값 또는 최소값을 삭제할 때는 해당 힙에서 삭제합니다. 
또한, 한 힙에서 값을 삭제할 때 다른 힙에서도 해당 값을 삭제하여 두 힙이 항상 동기화되도록 합니다.
'''

import heapq

def solution(operations):
    min_heap = []
    max_heap = []
    for operation in operations:
        op, num = operation.split()
        num = int(num)
        if op == 'I':
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
        elif num == 1 and max_heap:
            max_val = -heapq.heappop(max_heap)
            min_heap.remove(max_val)
        elif num == -1 and min_heap:
            min_val = heapq.heappop(min_heap)
            max_heap.remove(-min_val)
    if not min_heap:
        return [0, 0]
    else:
        return [-heapq.heappop(max_heap), heapq.heappop(min_heap)]