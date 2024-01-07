from collections import Counter

def solution(s):
    count = Counter(s)
    return ''.join(sorted([char for char in count if count[char] == 1]))

# 다른 풀이, 딕셔너리의 items() 메서드 이용
from collections import Counter

def solution(s):
    return ''.join(sorted(c for c, cnt in Counter(s).items() if cnt == 1))
