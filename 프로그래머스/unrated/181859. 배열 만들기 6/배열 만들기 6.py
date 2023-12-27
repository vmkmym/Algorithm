def solution(arr):
    stk = []

    for i in arr:
        if not stk:
            stk.append(i)
        elif stk[-1] == i:
            stk.pop()
        else:
            stk.append(i)

    return stk if stk else [-1]

# return stk or [-1] 로도 작성할 수 있음. 
# 객체1 or 객체2 연산은 bool(객체1)이 True이면 객체1을, False이면(비어 있으면) 객체2를 반환

# 다른 풀이
def solution(arr):
    stk = []
    i = 0
    
    while i < len(arr):
        if len(stk) == 0:
            stk.append(arr[i])
            i += 1
        elif stk[-1] == arr[i]:
            stk.pop()
            i += 1
        else:
            stk.append(arr[i])
            i += 1
            
    return stk if len(stk) > 0 else [-1]
