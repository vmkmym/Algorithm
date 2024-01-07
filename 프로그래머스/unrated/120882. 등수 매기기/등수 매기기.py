def solution(score):
    ranks = []

    for current in score:
        count = 1 
        for other in score:
            if (current[0] + current[1]) / 2 < (other[0] + other[1]) / 2:
                count += 1
        ranks.append(count) 

    return ranks

# 다른 사람 풀이
def solution(score):
    rank = sorted([sum(s) / 2 for s in score], reverse=True)
    rankDict = {}
    
    for i, r in enumerate(rank):
        if r not in rankDict.keys():
            rankDict[r] = i + 1
            
    return [rankDict[sum(s) / 2] for s in score]