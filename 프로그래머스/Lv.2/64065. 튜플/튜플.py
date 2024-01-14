def solution(s):
    s = s[2:-2] # {{, }} 제거
    s = s.split("},{") 
    s.sort(key=len) # 길이 순으로 정렬해야됨
    answer = []

    for i in s:
        ii = i.split(',')
        for j in ii: 
            if int(j) not in answer: 
                answer.append(int(j))
    return answer