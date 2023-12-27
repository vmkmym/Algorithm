def solution(n, k):
    return [i for i in range(1, n + 1) if i % k == 0]

# 다른 사람 풀이
# 배수라서 1부터 안해도 되고 k부터, k간격으로, n+1까지
def solution(n, k):
    return [i for i in range(k,n+1,k)]
