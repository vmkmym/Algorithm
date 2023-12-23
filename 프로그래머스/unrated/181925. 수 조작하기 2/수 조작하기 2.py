def solution(numLog):
    result = ''
    log = {1: 'w', -1: 's', 10: 'd', -10: 'a'}

    for i in range(1, len(numLog)): 
        diff = numLog[i] - numLog[i - 1]
        result += log[diff] if diff in log else ''

    return result

# 다른 풀이
def solution(numLog):
    diff = numLog[i] - numLog[i - 1]
    return "".join(["w" if diff == 1 else "s" if diff == -1 else "d" if diff == 10 else "a" for i in range(1, len(numLog))])

# 또 다른 풀이 : 근데 너무 효율 안좋음...
def solution(numLog):
    control = []
    
    for i in range(len(numLog)):
        diff = numLog[i] - (numLog[i - 1] if i > 0 else 0)

        if diff == 1:
            control.append('w')
        elif diff == -1:
            control.append('s')
        elif diff == 10:
            control.append('d')
        elif diff == -10:
            control.append('a')

    return ''.join(control)
