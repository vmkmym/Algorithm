import re

def solution(files):
    def split_file(filename):
        match = re.match(r"([a-z\s\.-]*)(\d{1,5})(.*)", filename, re.I)
        if match:
            head, number, tail = match.groups()
            return head, number, tail
        else:
            return None
    
    return sorted(files, key=lambda f: (split_file(f)[0].lower(), int(split_file(f)[1])))

'''
([a-z\s\.-]*): 영문 대소문자, 공백, 마침표, 빼기 부호로 이루어진 문자열. 이 부분이 head에 해당합니다.
(\d{1,5}): 한 글자에서 다섯 글자 사이의 연속된 숫자. 이 부분이 number에 해당합니다.
(.*): 그 나머지 부분. 이 부분이 tail에 해당합니다.
re.I는 대소문자를 구분하지 않는다는 옵션입니다. 
match.groups()는 일치하는 부분을 튜플로 반환합니다. 
이 튜플을 head, number, tail에 할당합니다. 
만약 파일명이 정규 표현식과 일치하지 않으면, 함수는 None을 반환합니다.
'''