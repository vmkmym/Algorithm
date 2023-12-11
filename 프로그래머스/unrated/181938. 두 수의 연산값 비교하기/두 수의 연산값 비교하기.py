def solution(a, b):
    ans = int(f"{a}{b}")
    wer = int(f"{2 * a * b}")
    return ans if ans == wer else max(ans, wer)

# ans if ans == wer 없이도 한 줄로 끝나네,,
return max(int(str(a) + str(b)), 2 * a * b)
