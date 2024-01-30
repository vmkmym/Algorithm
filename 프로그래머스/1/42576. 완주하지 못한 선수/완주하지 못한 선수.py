from collections import Counter
# 시간 복잡도가 O(n)
def solution(participant, completion):
    participant_count = Counter(participant)
    completion_count = Counter(completion)
    
    for name, count in participant_count.items():
        if completion_count[name] != count:
            return name

# 다른 사람 풀이 : 시간 복잡도가 O(n)
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

# 해시 함수를 이용한 풀이 : 시간 복잡도가 O(n)
def solution(participant, completion):
    answer = 0
    temp = {}
    for part in participant:
        p_hash = hash(part) # 각 이름을 해시 함수에 통과시켜 해시 값을 구한다.
        answer += p_hash # 해시 값을 모두 더한다.
        temp[p_hash] = part # 해시 값을 키로, 이름을 값으로 딕셔너리에 저장한다.
    for comp in completion:
        answer -= hash(comp) # 완주한 사람의 해시 값을 빼준다.
    return temp[answer] # 해시 값을 통해 완주하지 못한 사람을 찾아 반환한다.