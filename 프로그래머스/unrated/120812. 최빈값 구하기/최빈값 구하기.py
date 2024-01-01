import statistics

def solution(array):
    modes = statistics.multimode(array)
    return -1 if len(modes) > 1 else modes[0]

# mode로 풀이 시도해봤는데 최빈값이 여러 개 일 때를 통과못함
# 근데 multimode라는게 있었음
# statistics.multimode() 함수는 여러 개의 최빈값을 리스트로 반환한다

# 다른 사람 풀이
# 배열에서 중복된 원소를 제거하면서 남은 원소를 반환함
def solution(array):
    while len(array) != 0:
        for i, a in enumerate(set(array)):
            array.remove(a)
        if i == 0: return a
    return -1


# 다른 사람 풀이
# 컬렉션 사용한 풀이 : defaultdict
from collections import defaultdict

def solution(array):   
    mode_counts = defaultdict(list)

    for v in set(array):
        mode_counts[array.count(v)].append(v)

    return mode_counts[max(mode_counts)][0] if len(mode_counts[max(mode_counts)]) == 1 else -1

# 다른 사람 풀이
# 컬렉션 사용한 풀이 : Counter
from collections import Counter

def solution(array):
    a = Counter(array).most_common(2)
    if len(a) == 1:
        return a[0][0]
    if a[0][1] == a[1][1]:
        return -1
    return a[0][0]
