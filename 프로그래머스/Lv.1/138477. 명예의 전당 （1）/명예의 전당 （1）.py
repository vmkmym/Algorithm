import heapq

def solution(k, score):
    fame = []
    result = [] 

    for s in score:
        if len(fame) < k:
            heapq.heappush(fame, s)
        elif fame[0] < s:
            heapq.heappop(fame)
            heapq.heappush(fame, s)
        result.append(fame[0])

    return result