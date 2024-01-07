def solution(lines):
    occurrences = 0  # 겹치는 숫자들의 발생 횟수를 저장할 변수
    counts = {}  # 각 숫자의 선분에서의 발생 횟수를 저장할 딕셔너리
    
    for line in lines:
        for num in range(line[0], line[1]):
            counts[num] = counts.get(num, 0) + 1  # 각 숫자의 발생 횟수를 1씩 증가
        
    for count in counts.values():
        if count >= 2:
            occurrences += 1  # 발생 횟수가 2번 이상인 경우에만 카운트
    
    return occurrences