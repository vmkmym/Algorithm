def solution(l, r):
    result = [num for num in range(l, r+1) if set(str(num)) <= {'0', '5'}] or [-1]
    
    # sorted()에서 정렬의 기준을 지정하는 방법
    return sorted(result, key=lambda x: int(x))

# 시간 무슨 일이지.. 근데 점수는 높다..
# 파이썬에서 sorted 사용할 때 정렬 기준을 람다식으로 지정한다는 것을 처음 알게 됨
# set은 중복값 허용x, 순서x, 변경불가능 컬렉션으로 {}를 쓰고 쉼표로 구분
