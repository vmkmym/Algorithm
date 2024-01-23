def solution(X, Y):
    X = sorted(str(X))
    Y = sorted(str(Y))
    
    result = []
    i = j = 0
    
    while i < len(X) and j < len(Y):
        if X[i] == Y[j]:
            result.append(X[i])
            i += 1
            j += 1
        elif X[i] < Y[j]:
            i += 1
        else:
            j += 1

    if not result:
        return '-1'

    result = ''.join(sorted(result, reverse=True))

    if set(result) == {'0'}:
        return '0'

    return result