def solution(arr, query):
    for i, e in enumerate(query):
        if i % 2 == 0:
            arr = [arr[j] for j in range(len(arr)) if j <= e]
        else:
            arr = [arr[j] for j in range(len(arr)) if j >= e]
    return arr


# 다른 풀이
def solution(arr, query):
    for i, e in enumerate(query):
        if i % 2 == 0:
            arr = arr[:e+1]
        else:
            arr = arr[e:]
    return arr

# 다른 풀이
def solution(arr, query):
    start = 0
    end = len(query) - 1
    answer = arr[start:end]

    for i in range(len(query)):
        if i % 2 == 0:
            end = start + query[i]
        else:
            start += query[i]
                
    if not answer:
        return [-1]
        
    return answer

# 다른 풀이
def solution(arr, query):
    s, e = 0, 0
    for i in range(len(query)):
        if i % 2:
            s += query[i]
        else:
            e = s + query[i]

    return arr[s:e] if s != e else [-1]

# 이 문제는 어려웠는데, 원본 배열에 쿼리를 적용해서 순회하는 것이라서 어려웠음 -> 매번 처리할 query의 값과 처리 전 후의 arr의 상태
# 다른 사람 풀이에서 빈 리스트이면 -1을 반환하는데 나는 이 코드를 넣지 않았음
# 2번째 풀이가 내가 생각했던 방법이었는데 나는 인덱스에서 실수를 했나봄
# 4번째 풀이도 간결해서 좋은 듯
