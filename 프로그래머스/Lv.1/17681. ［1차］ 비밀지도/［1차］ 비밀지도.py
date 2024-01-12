def solution(n, arr1, arr2):
    result = []

    for r1, r2 in zip(arr1, arr2):
        binary = bin(r1 | r2)[2:].zfill(n)
        row = ''.join(['#' if bit == '1' else ' ' for bit in binary])
        result.append(row)
    
    return result

'''
이렇게 줄일수도 있음
def solution(n, arr1, arr2):
    return [''.join(['#' if bit == '1' else ' ' for bit in bin(r1 | r2)[2:].zfill(n)]) for r1, r2 in zip(arr1, arr2)]
'''