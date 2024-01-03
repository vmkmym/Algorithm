def solution(arr, idx):
    if 1 not in arr[idx:]:
        return -1
    
    for i in range(idx, len(arr)):
        if arr[i] == 1:
            return i

# 다른 사람 풀이
'''
index() 함수는 리스트(List)나 튜플(Tuple)에서 특정 요소의 인덱스를 찾는 데 사용됩니다. 
이 함수는 해당 요소의 첫 번째 등장하는 인덱스를 반환합니다.

list_name.index(element, start, end)

list_name: 인덱스를 찾을 리스트 이름
element: 리스트에서 찾을 요소
start (옵션): 찾기 시작할 인덱스(default: 0)
end (옵션): 찾을 범위의 끝 인덱스(default: 리스트의 끝)
'''
def solution(arr, idx):
    answer = 0
    try:
        answer = arr.index(1, idx)
    except:
        answer = -1

    return answer
