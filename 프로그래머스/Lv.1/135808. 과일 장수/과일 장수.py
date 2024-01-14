def solution(k, m, score):
    profit = 0
    score.sort(reverse=True)
    box = [score[i:i+m] for i in range(0, len(score), m) if len(score[i:i+m]) == m]
    for i in range(len(box)):
        profit += min(box[i]) * m
    return profit