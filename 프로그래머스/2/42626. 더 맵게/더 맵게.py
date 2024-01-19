import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    for i in range(len(scoville)):
        if scoville[0] >= K:
            break
        if len(scoville) == 1:
            return -1
        new = heapq.heappop(scoville) + heapq.heappop(scoville) * 2
        heapq.heappush(scoville, new)
        answer += 1
    return answer