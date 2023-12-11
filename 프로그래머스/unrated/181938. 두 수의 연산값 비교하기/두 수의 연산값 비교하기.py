def solution(a, b):
    ans = int(f"{a}{b}")
    wer = int(f"{2 * a * b}")
    return ans if ans == wer else max(ans, wer)