import re

def solution(babbling):
    answer = 0
    
    for char in babbling:
        if re.match(r"^(aya|ye|woo|ma)+$", char):
            answer += 1
            
    return answer

# 다른 사람 코드로 제출
'''
re.match() 함수는 Python의 re(Regular Expression, 정규 표현식) 모듈에서 제공하는 함수 중 하나입니다. 
이 함수는 주어진 패턴이 문자열의 시작 부분과 일치하는지 확인합니다.
re.match(pattern, string)
'''