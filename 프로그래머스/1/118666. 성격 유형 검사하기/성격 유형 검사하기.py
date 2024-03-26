def solution(survey, choices):
    kakao_test = ["RT", "CF", "JM", "AN"]
    score = {1: 3, 2: 2, 3: 1, 5: 1, 6: 2, 7: 3}
    test = {}

    for i, j in zip(survey, choices):
        diagree, agree = i[0], i[1]

        if j in [1, 2, 3]:
            if diagree in test:
                test[diagree] += score[j]
            else:
                test[diagree] = score[j]
        elif j in [5, 6, 7]:
            if agree in test:
                test[agree] += score[j]
            else:
                test[agree] = score[j]

    answer = []
    for case in kakao_test:
        max_score = max(test.get(case[0], 0), test.get(case[1], 0))
        for c in case:
            if test.get(c, 0) == max_score:
                answer.append(c)
                break

    return "".join(answer)