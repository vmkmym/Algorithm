def solution(q, r, code):
    return ''.join([code[i] for i in range(len(code)) if i % q == r])

# 진짜 천재들인가?
def solution(q, r, code):
    return code[r::q]