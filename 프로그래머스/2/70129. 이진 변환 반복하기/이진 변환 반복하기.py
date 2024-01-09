def solution(s):
    count = 0
    erased = 0
    
    while s != "1":
        erased += s.count("0")
        s = s.replace("0", "")
        s = format(len(s), 'b')
        count += 1
    
    return [count, erased]

# format() 함수를 사용하여 정수를 원하는 형식으로 변환