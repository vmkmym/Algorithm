def solution(s):
    answer = ""
    
    for word in s.split(" "):
        for idx, char in enumerate(word):
            if idx % 2 == 0:
                answer += char.upper()
            else:
                answer += char.lower()
        answer += " "
        
    return answer[:-1]
