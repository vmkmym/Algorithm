import heapq

def solution(n, works):
    works = [-work for work in works] # 최소 힙을 구하기 위해 음수로 변환
    heapq.heapify(works) # 최소 힙으로 변환

    for _ in range(n):
        max_work = heapq.heappop(works) # 최소 힙이므로 가장 작은 값이 pop
        if max_work == 0: # 모든 작업량이 0이면 종료
            break
        heapq.heappush(works, max_work + 1)

    return sum(work ** 2 for work in works)