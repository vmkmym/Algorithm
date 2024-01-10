def solution(s):
    answer = []
    position = {}
    
    for idx, char in enumerate(s):
        if char not in position:
            answer.append(-1)
        else:
            answer.append(idx - position[char])
        position[char] = idx
        
    return answer