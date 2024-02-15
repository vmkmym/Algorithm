import re

def solution(babbling):
    answer = 0
    
    for char in babbling:
        # 정규식을 이용하여 문자열이 aya, ye, woo, ma로만 이루어져 있고, aya, ye, woo, ma가 연속으로 나오지 않는지 확인
        if re.fullmatch(r"(aya|ye|woo|ma)+", char) and not re.search(r"(aya){2,}|(ye){2,}|(woo){2,}|(ma){2,}", char):
            answer += 1
            
    return answer