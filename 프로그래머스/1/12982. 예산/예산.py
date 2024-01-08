def solution(d, budget):
    d.sort()
    count = 0

    for i in range(len(d)):
        if d[i] <= budget:
            budget -= d[i]
            count += 1
        
    return count