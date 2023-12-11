def solution(a, b):
    ans = int(''.join([str(a), str(b)]))
    wer = int(''.join([str(b), str(a)]))
    return max(ans, wer)

# 다른 사람 풀이 참고: f문자열포맷
return int(max(f"{a}{b}", f"{b}{a}"))
