import re

def solution(myString, pat):
    pattern = re.compile(f'(?=({pat}))')
    matches = pattern.finditer(myString)
    return sum(1 for _ in matches)

'''
 re.compile()을 사용하여 pat을 찾는 정규표현식을 설정하고, 
 finditer() 함수를 사용하여 겹치는 부분 문자열을 찾음
 
 (?= ...)는 정규표현식에서 전방 탐색(lookahead) 기능을 사용하는 것으로, 
 해당 패턴과 일치하는 부분 문자열을 찾음
 '''


'''
def solution(myString, pat):
    count = 0
    start = 0
    
    while True:
        index = myString.find(pat, start)
        if index == -1:
            break
        count += 1
        start = index + 1
    
    return count
'''