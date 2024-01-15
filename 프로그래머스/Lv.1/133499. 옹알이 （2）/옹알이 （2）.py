import re

def solution(babbling):
    answer = 0
    
    for char in babbling:
        if re.fullmatch(r"(aya|ye|woo|ma)+", char) and not re.search(r"(aya){2,}|(ye){2,}|(woo){2,}|(ma){2,}", char):
            answer += 1
            
    return answer