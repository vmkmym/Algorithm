# 버블 정렬 구현하기
def bubble_sort(arr):
    length = len(arr)-1
    for i in range(length):
        swap = False
        for j in range(length-i):
            if arr[j] > arr[j+1]: 
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap = True
        if swap == False:
            break
    return arr