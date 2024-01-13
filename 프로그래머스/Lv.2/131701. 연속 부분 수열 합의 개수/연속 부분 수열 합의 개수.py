def solution(elements):
    length = len(elements)
    sums = set()
    
    for i in range(length):
        sum = 0
        for j in range(length):
            sum += elements[(i + j) % length]
            sums.add(sum)
            
    return len(sums)