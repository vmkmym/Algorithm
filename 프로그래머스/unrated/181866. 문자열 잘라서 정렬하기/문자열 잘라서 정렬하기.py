def solution(myString):
    return sorted(filter(None, myString.split('x')))

# filter()로 빈문자열 제거