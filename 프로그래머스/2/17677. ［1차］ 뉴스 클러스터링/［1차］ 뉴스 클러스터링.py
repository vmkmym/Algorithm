import math
import collections
import re

def solution(str1, str2):
    str1 = [str1[i:i+2].lower() for i in range(len(str1)-1) if re.match('[a-z]{2}', str1[i:i+2].lower())] 
    str2 = [str2[i:i+2].lower() for i in range(len(str2)-1) if re.match('[a-z]{2}', str2[i:i+2].lower())]
    
    counter1 = collections.Counter(str1) 
    counter2 = collections.Counter(str2)
    
    intersection = list((counter1 & counter2).elements()) # 교집합
    union = list((counter1 | counter2).elements()) # 합집합

    if len(union) == 0:
        return 65536
    else:
        similarity = len(intersection) / len(union) # 자카드 유사도
        return math.floor(similarity * 65536)

# re.match(pattern, string)
    # string이 pattern 정규 표현식으로 시작하는지 확인합니다. 
    # 만약 시작한다면 match 객체를 반환하고, 그렇지 않다면 None을 반환합니다.

# '[a-z]{2}'
    # 이 정규 표현식은 소문자 알파벳 두 글자를 의미합니다. 
    # [a-z]는 소문자 알파벳 중 하나를, {2}는 바로 앞의 패턴이 정확히 두 번 반복되어야 함을 의미합니다.
    
# re 모듈의 주요 함수
    # re.search(pattern, string): 문자열 전체에서 패턴과 일치하는 부분을 찾습니다. 일치하는 경우 첫 번째 일치 항목에 대한 match 객체를 반환하고, 그렇지 않으면 None을 반환합니다.
    # re.findall(pattern, string): 문자열에서 패턴과 일치하는 모든 부분을 찾아 리스트로 반환합니다.
    # re.sub(pattern, repl, string): 문자열에서 패턴과 일치하는 부분을 다른 문자열로 대체합니다.

# elements() 메소드는 collections.Counter 객체의 각 요소를 그 요소의 개수만큼 반복하여 반환하는 이터레이터를 생성