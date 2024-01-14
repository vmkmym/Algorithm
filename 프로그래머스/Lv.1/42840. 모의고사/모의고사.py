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