def solution(arr, queries):
    for i, j in queries:
        arr[i], arr[j] = arr[j], arr[i]
    return arr

# queries의 원소를 arr에 대입해서 값을 바꾸기
