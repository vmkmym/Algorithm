import re

def solution(myStr):
    result = re.split("[abc]+", myStr)
    return [elem for elem in result if elem] if result else ["EMPTY"]

'''
re.split("[abc]+", myStr)는 정규표현식 패턴 "[abc]+"을 이용하여 
"a", "b", "c" 중 하나 이상의 연속된 문자열을 구분자로 하여 문자열을 나눕니다.
'''