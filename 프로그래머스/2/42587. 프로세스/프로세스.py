from collections import deque

def solution(priorities, location):
    answer = 0
    priorities = deque(priorities)
    
    while True:
        if priorities[0] == max(priorities):
            answer += 1
            if location == 0:
                return answer
            priorities.popleft()
            location -= 1
        else:
            priorities.append(priorities.popleft())
            location = (location - 1) % len(priorities)