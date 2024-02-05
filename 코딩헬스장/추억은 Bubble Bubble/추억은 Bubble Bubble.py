# 버블 정렬 구현하기
def bubble_sort(arr):
    length = len(arr)-1 # 맨 마지막 요소는 제외
    for i in range(length):
        swap = False
        for j in range(length-i): # i까지는 제외하고 크기 비교
            if arr[j] > arr[j+1]: 
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap = True
        if swap == False:
            break
    return arr