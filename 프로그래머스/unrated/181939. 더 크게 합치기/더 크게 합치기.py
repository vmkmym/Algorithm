def solution(a, b):
    ans = int(''.join([str(a), str(b)]))
    wer = int(''.join([str(b), str(a)]))
    return max(ans, wer)

    