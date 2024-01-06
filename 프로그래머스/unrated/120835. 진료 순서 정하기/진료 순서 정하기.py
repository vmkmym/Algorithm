def solution(emergency):
    rank = [sorted(emergency, reverse=True).index(x) + 1 for x in emergency]
    return rank