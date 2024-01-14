from collections import deque
from math import ceil

def solution(progresses, speeds):
    release = deque(ceil((100 - p) / s) for p, s in zip(progresses, speeds))
    answer = []
    
    while release:
        count = 1
        r = release.popleft() 
        while release and r >= release[0]: 
            release.popleft() 
            count += 1 
        answer.append(count)
        
    return answer