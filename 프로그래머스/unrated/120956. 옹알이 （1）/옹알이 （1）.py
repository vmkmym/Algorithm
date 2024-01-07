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

# 다른 풀이
import re

def solution(babbling):
    regex = re.compile('^(aya|ye|woo|ma)+$')
    cnt=0
    for e in babbling:
        if regex.match(e):
            cnt+=1
    return cnt

# 다른 풀이
def solution(babbling):
    arr = [ "aya", "ye", "woo", "ma"]
    answer = 0
    for i in babbling:
        for j in arr:
            if j + j in i:
                break
            else:
                i = i.replace(j,'')
        if len(i) == 0:
            answer += 1
    return answer

# 음 역시 어려움..
