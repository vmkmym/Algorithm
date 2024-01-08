from itertools import combinations

def solution(number):
    return len(list(filter(lambda x: x[0] + x[1] + x[2] == 0, combinations(number, 3))))

# bard에게 줄여달라고 한 코드

''' 처음 코드
def solution(number):
    students = list(combinations(number, 3))
    count = 0
    for student in students:
        total = student[0] + student[1] + student[2]
        if total == 0:
            count += 1
    return count
'''
