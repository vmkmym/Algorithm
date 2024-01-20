def solution(n, s):
    if n > s:
        return [-1]
    r, d = divmod(s, n) 
    answer = [r] * n
    for i in range(d): # 나머지를 더하기
        answer[-1-i] += 1
    return answer