def solution(score):
    ranks = []

    for current in score:
        count = 1 
        for other in score:
            if (current[0] + current[1]) / 2 < (other[0] + other[1]) / 2:
                count += 1
        ranks.append(count) 

    return ranks