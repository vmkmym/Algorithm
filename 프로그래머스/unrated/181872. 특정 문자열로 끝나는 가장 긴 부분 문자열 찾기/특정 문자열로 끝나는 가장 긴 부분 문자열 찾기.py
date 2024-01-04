def solution(myString, pat):
    i = myString.rfind(pat)
    
    if i != -1:
        return myString[:i+len(pat)]
    else:
        return ""

# rfind()를 사용하여 "dE"가 마지막으로 나타나는 인덱스를 찾고, 해당 위치까지의 부분 문자열을 반환