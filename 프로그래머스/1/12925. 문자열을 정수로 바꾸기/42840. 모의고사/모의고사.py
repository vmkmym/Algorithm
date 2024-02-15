def solution(answers):
    correct_person = []
    correct_cnt = [0, 0, 0]
    pattern1 = [1, 2, 3, 4, 5]
    pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    # 정답 개수를 세는 반복문
    for i in range(len(answers)):
        if answers[i] == pattern1[i % 5]:
            correct_cnt[0] += 1
        if answers[i] == pattern2[i % 8]:
            correct_cnt[1] += 1
        if answers[i] == pattern3[i % 10]:
            correct_cnt[2] += 1
    # 가장 많이 맞춘 사람을 찾는 반복문
    for i in range(3):
        if correct_cnt[i] == max(correct_cnt):
            correct_person.append(i + 1)
    correct_person.sort()
    return correct_person

# 다른 사람 풀이
from itertools import cycle # 이건 처음봄... cycle이라는 함수가 있었구나

def solution(answers):
    giveups = [
        cycle([1,2,3,4,5]),
        cycle([2,1,2,3,2,4,2,5]),
        cycle([3,3,1,1,2,2,4,4,5,5]),
    ]
    scores = [0, 0, 0]
    for num in answers:
        for i in range(3):
            if next(giveups[i]) == num:
                scores[i] += 1
    highest = max(scores)

    return [i + 1 for i, v in enumerate(scores) if v == highest]