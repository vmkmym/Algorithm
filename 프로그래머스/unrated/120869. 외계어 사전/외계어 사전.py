from itertools import permutations

def solution(spell, dic):
    for perm in permutations(spell):  
        word = ''.join(perm) 
        if word in dic:
            return 1 
    return 2 

# itertools의 permutations
# permutations() : 이터레이터
# p[, r] : 인자
# r-길이 튜플들, 모든 가능한 순서, 반복되는 요소 없음 : 결과
# 예) permutations('ABCD', 2)
# > AB AC AD BA BC BD CA CB CD DA DB DC