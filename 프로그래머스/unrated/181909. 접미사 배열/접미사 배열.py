def solution(my_string):
    return sorted([my_string[i:] for i in range(len(my_string))])

# 다른 사람 풀이
solution = lambda my_string : sorted( [my_string[i:] for i in range(len(my_string))])

# 리스트 정렬
sorted()와 sort()
    리스트의 요소를 정렬하지만 동작 방식과 사용 방법에 차이가 있음

sort()
    이 메서드는 리스트 자체를 변경하며, 리스트의 요소를 인-place(현재 위치에서)로 정렬합니다. 
    따라서 sort() 메서드는 원래의 리스트를 변경하고, 반환 값은 None입니다. 
        
sorted()
    이 함수는 새로운 정렬된 리스트를 반환하며, 원본 리스트를 변경하지 않습니다. 
    원본 리스트는 그대로 유지됩니다.
