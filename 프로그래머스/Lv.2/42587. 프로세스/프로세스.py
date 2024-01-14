def solution(priorities, location):
    answer = 0
    while True:
        if priorities[0] == max(priorities): # 가장 앞에 있는 프로세스의 중요도가 가장 높은 경우
            answer += 1 
            if location == 0: 
                return answer
            else: 
                priorities.pop(0) 
                location -= 1 
        else: # 가장 앞에 있는 프로세스의 중요도가 가장 높지 않은 경우
            priorities.append(priorities.pop(0))
            location -= 1 
            if location < 0: 
                location = len(priorities) - 1 # location이 0보다 작아지면 가장 뒤로 보냄
    return answer