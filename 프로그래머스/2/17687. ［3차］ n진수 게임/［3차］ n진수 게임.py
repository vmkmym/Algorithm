def convert(n, base): # n을 base진수로 변환
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)
    if q == 0: # 몫이 0이면
        return T[r] # 나머지를 반환
    else: # 몫이 0이 아니면
        return convert(q, base) + T[r] # 재귀호출하여 몫을 계속 변환

def solution(n, t, m, p):
    total = ""
    i = 0 # 말해야 하는 숫자
    while len(total) < m * t:
        total += convert(i, n)
        i += 1 # 다음 숫자
    return total[p-1::m][:t] # 0부터 m간격으로 t개의 숫자를 뽑음