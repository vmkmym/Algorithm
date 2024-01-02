def solution(arr):
    result = []
    
    for a in arr:
        result.extend([a] * a)
        
    return result

# extend() 함수는 리스트에 다른 리스트나 이터러블(iterable)의 모든 항목을 추가하는 데 사용됩니다. 
# 기존 리스트에 다른 리스트나 이터러블의 모든 요소를 개별 항목으로 추가하고자 할 때 유용하게 활용됩니다.