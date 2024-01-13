# from collections import Counter

# def solution(k, tangerine):
#     count = Counter(tangerine)
#     sorted_tangerine = sorted(tangerine, key=lambda x: (-count[x], tangerine.index(x)))

#     return len(set(sorted_tangerine[:k]))

def solution(k, tangerine):
    answer = 0
    dic = {}
    r = 0
    
    # 딕셔너리에 key, value 형태로 값 넣음
    for i in tangerine:
        d = dic.get(i)
        if d == None:
            dic[i] = 1
        else:
            dic[i] += 1
    
    # value만 추출하여 내림차순으로 값 정렬
    dic = sorted(dic.values(), reverse=True)
    
    # k와 비교하며 count
    for i in dic:
        r += i
        answer += 1
        if k <= r: # k보다 같거나 크면 종료
            break
    return answer
