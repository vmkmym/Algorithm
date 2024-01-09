# JadenCase란 모든 단어의 첫 문자가 대문자이고, 그 외의 알파벳은 소문자인 문자열
def solution(s):
    words = s.split(' ')
    jadenCase = ''
    
    for i, word in enumerate(words):
        if word:
            words[i] = word[0].upper() + word[1:].lower()
        else:
            words[i] = ''

    for i in range(len(words)):
        jadenCase += words[i]
        if i != len(words) - 1:
            jadenCase += ' '
            
    return jadenCase

# 공백의 개수도 유지해줘야 통과됨

'''Python String Method

capitalize() - 첫 글자를 대문자로 변환합니다.
casefold() - 문자열을 소문자로 변환합니다.
center() - 가운데 정렬된 문자열을 반환합니다.
count() - 지정된 값이 문자열에서 몇 번 나오는지 개수를 반환합니다.
encode() - 문자열의 인코딩된 버전을 반환합니다.

endswith() - 문자열이 지정된 값으로 끝나는지 여부를 반환합니다.
expandtabs() - 탭의 크기를 지정한 만큼 확장한 문자열을 반환합니다.
find() - 지정된 값이 문자열에서 처음으로 나오는 위치를 반환합니다.
format() - 문자열 내에서 지정된 값을 형식화하여 반환합니다.
format_map() - 문자열 내에서 지정된 값을 형식화하여 반환합니다.

index() - 지정된 값이 문자열에서 처음으로 나오는 위치를 반환합니다.
isalnum() - 문자열의 모든 문자가 알파벳 또는 숫자인지 여부를 반환합니다.
isalpha() - 문자열의 모든 문자가 알파벳인지 여부를 반환합니다.
isascii() - 문자열의 모든 문자가 ASCII 문자인지 여부를 반환합니다.
isdecimal() - 문자열의 모든 문자가 10진수인지 여부를 반환합니다.

isdigit() - 문자열의 모든 문자가 숫자인지 여부를 반환합니다.
isidentifier() - 문자열이 식별자인지 여부를 반환합니다.
islower() - 문자열의 모든 문자가 소문자인지 여부를 반환합니다.
isnumeric() - 문자열의 모든 문자가 숫자인지 여부를 반환합니다.
isprintable() - 문자열의 모든 문자가 출력 가능한지 여부를 반환합니다.

isspace() - 문자열의 모든 문자가 공백인지 여부를 반환합니다.
istitle() - 문자열이 타이틀 형식에 맞는지 여부를 반환합니다.
isupper() - 문자열의 모든 문자가 대문자인지 여부를 반환합니다.
join() - 반복 가능한 객체의 요소를 문자열로 연결합니다.
ljust() - 문자열을 왼쪽 정렬한 버전을 반환합니다.

lower() - 문자열을 소문자로 변환합니다.
lstrip() - 문자열 왼쪽에서 지정된 문자를 제거한 버전을 반환합니다.
maketrans() - 번역에 사용할 번역 테이블을 반환합니다.
partition() - 문자열을 세 부분으로 나눈 튜플을 반환합니다.
replace() - 지정된 값을 다른 값으로 대체한 문자열을 반환합니다.

rfind() - 지정된 값이 문자열에서 마지막으로 나오는 위치를 반환합니다.
rindex() - 지정된 값이 문자열에서 마지막으로 나오는 위치를 반환합니다.
rjust() - 문자열을 오른쪽 정렬한 버전을 반환합니다.
rpartition() - 문자열을 세 부분으로 나눈 튜플을 반환합니다.
rsplit() - 문자열을 지정된 구분자로 나눈 뒤 리스트로 반환합니다.

rstrip() - 문자열 오른쪽에서 지정된 문자를 제거한 버전을 반환합니다.
split() - 문자열을 지정된 구분자로 나눈 뒤 리스트로 반환합니다.
splitlines() - 문자열을 줄 바꿈 기준으로 나눈 뒤 리스트로 반환합니다.
startswith() - 문자열이 지정된 값으로 시작하는지 여부를 반환합니다.
strip() - 문자열의 양쪽에서 지정된 문자를 제거한 버전을 반환합니다.

swapcase() - 대소문자를 바꾼 문자열을 반환합니다.
title() - 각 단어의 첫 글자를 대문자로 변환한 문자열을 반환합니다.
translate() - 번역된 문자열을 반환합니다.
upper() - 문자열을 대문자로 변환합니다.
zfill() - 지정된 개수의 0으로 문자열을 채웁니다.
'''
