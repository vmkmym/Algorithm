def solution(rank, attendance):
    students = [] 

    for i, rank_value in enumerate(rank):
        if attendance[i]:
            students.append((rank_value, i))

    students.sort()
    result = students[0][1] * 10000 + students[1][1] * 100 + students[2][1]
    
    return result