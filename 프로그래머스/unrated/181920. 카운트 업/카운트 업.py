def solution(start_num, end_num):
    return [num for num in range(start_num, end_num + 1)]

# 다른 풀이
# range를 for문에서만 쓰는 걸로 생각했는데 이렇게도 사용할 수 있구나 알게 됨
# return에 바로 리스트 컴프리헨션 써서 이 보다 짧기는 힘들 것 같았는데 list 쓰니까 좋다.
# 하지만 가독성과 유지보수 측면에서는 list(), range() 함수를 쓰는 것이 명확하다.
# 특히 복잡한 조건이나 반복 작업이 있는 경우에는 리스트 컴프리헨션보다는 일반적인 for 반복문을 사용하는 것이 코드를 이해하기 쉽다고 함
def solution(start_num, end_num):
    return list(range(start_num, end_num + 1))
