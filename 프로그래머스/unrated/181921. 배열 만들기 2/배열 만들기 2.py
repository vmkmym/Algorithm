def solution(l, r):
    result = [num for num in range(l, r+1) if set(str(num)) <= {'0', '5'}] or [-1]
    
    # sorted()에서 정렬의 기준을 지정하는 방법
    return sorted(result, key=lambda x: int(x))
