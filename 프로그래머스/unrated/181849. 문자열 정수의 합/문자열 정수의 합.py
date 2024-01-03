def solution(num_str):
    return sum(int(num) for num in num_str)

# 다른 사람 풀이
# 문자열은 이미 리스트임
# map 사용법 알아둘 것
'''
map(function, iterable1, iterable2, ...)

function: 적용하고자 하는 함수
iterable1, iterable2, ... : 함수를 적용할 하나 이상의 순회 가능한(iterable) 객체

map() 함수는 첫 번째 인자로 전달된 함수를 두 번째 이후의 모든 iterable에 적용하고, 
그 결과로 각 iterable에 있는 요소들을 인자로 받은 함수에 적용한 새로운 iterator를 반환합니다.
'''
def solution(num_str):
    return sum(map(int, num_str))
