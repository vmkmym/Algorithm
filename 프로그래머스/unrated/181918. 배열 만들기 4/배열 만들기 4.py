def solution(arr):
    stk = []
    i = 0
    
    while i < len(arr):
        if len(stk) == 0:
            stk.append(arr[i])
            i += 1
        elif len(stk) != 0 and stk[-1] < arr[i]:
            stk.append(arr[i])
            i += 1
        elif len(stk) != 0 and stk[-1] >= arr[i]:
            stk.pop()
    
    return stk

# 음 뭐지 왜 5점이지?

# gpt 풀이, 다른 사람 풀이도 이거랑 비슷함
# 입력 배열을 한 번 순회하는 선형 시간복잡도를 갖고 있으므로 입력 크기에 대해 효율적임
def solution(arr):
    stk = []
    
    for num in arr:
        while stk and stk[-1] <= num:
            stk.pop()
        stk.append(num)
    
    return stk
