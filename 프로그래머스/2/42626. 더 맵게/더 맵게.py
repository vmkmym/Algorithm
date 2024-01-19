import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    for i in range(len(scoville)):
        if scoville[0] >= K:
            break
        if len(scoville) == 1: # 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우에는 -1을 return
            return -1
        new = heapq.heappop(scoville) + heapq.heappop(scoville) * 2
        heapq.heappush(scoville, new)
        answer += 1
    return answer