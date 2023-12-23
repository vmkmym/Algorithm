def solution(numLog):
    result = ''
    log = {1: 'w', -1: 's', 10: 'd', -10: 'a'}

    for i in range(1, len(numLog)): 
        diff = numLog[i] - numLog[i - 1]
        result += log[diff] if diff in log else ''

    return result