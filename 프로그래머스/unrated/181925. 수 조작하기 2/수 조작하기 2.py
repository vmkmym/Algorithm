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
