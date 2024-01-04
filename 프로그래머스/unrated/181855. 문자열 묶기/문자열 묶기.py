from collections import defaultdict
# collections - Container datatypes

def solution(strArr):
    groups = defaultdict(int)

    for s in strArr:
        groups[len(s)] += 1

    return max(groups.values()) if groups else 0

# Setting the default_factory to int makes the defaultdict useful for counting 
# (like a bag or multiset in other languages):
s = 'mississippi'
d = defaultdict(int)
for k in s:
    d[k] += 1
    
sorted(d.items())

[('i', 4), ('m', 1), ('p', 2), ('s', 4)]

# Setting the default_factory to set makes the defaultdict useful for building a dictionary of sets:
s = [('red', 1), ('blue', 2), ('red', 3), ('blue', 4), ('red', 1), ('blue', 4)]
d = defaultdict(set)
for k, v in s:
    d[k].add(v)

sorted(d.items())

[('blue', {2, 4}), ('red', {1, 3})]


'''
- namedtuple() : 명명된 필드를 가진 튜플 서브클래스를 만드는 팩토리 함수
- deque : 양쪽 끝에서 빠르게 추가하고 삭제할 수 있는 리스트와 유사한 컨테이너
- ChainMap : 여러 매핑의 단일 뷰를 생성하는 dict와 유사한 클래스
- Counter : 해시 가능한 객체를 카운팅하는 dict 서브클래스
- OrderedDict : 항목이 추가된 순서를 기억하는 dict 서브클래스
- defaultdict : 빠진 값들을 제공하기 위해 팩토리 함수를 호출하는 dict 서브클래스
- UserDict : 쉬운 dict 서브클래싱을 위한 사전 객체 래퍼
- UserList : 쉬운 list 서브클래싱을 위한 리스트 객체 래퍼
- UserString : 쉬운 string 서브클래싱을 위한 문자열 객체 래퍼
'''