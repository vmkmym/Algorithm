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
        # case: RT , max_score: 6
        # case: CF , max_score: 0
        # case: JM , max_score: 0
        # case: AN , max_score: 0
        
        for c in case: # c가 없으면 기본값 0을 가져옴
            if test.get(c, 0) == max_score:
                answer.append(c)
                break # 그래서 둘 다 0인 경우는 첫번째 문자에서 break되기 때문에 앞에 있는 문자가 answer에 추가된다.
                # c: R , test.get(c, 0): 6
                # c: T , test.get(c, 0): 1
                # c: C , test.get(c, 0): 0
                # c: F , test.get(c, 0): 0
                # c: J , test.get(c, 0): 0
                # c: M , test.get(c, 0): 0
                # c: A , test.get(c, 0): 0
                # c: N , test.get(c, 0): 0
                # answer:  ['R', 'C', 'J', 'A']

    return "".join(answer) 

print(solution(["TR", "RT", "TR"],[7, 1, 3])) # "RCJA"

# from collections import defaultdict

# def solution(survey, choices):
#     kakao_test = ["RT", "CF", "JM", "AN"]
#     score = [0, 3, 2, 1, 0, 1, 2, 3]
#     test = defaultdict(int)

#     for i, j in zip(survey, choices):
#         diagree, agree = i[0], i[1]

#         if j in [1, 2, 3]:
#             test[diagree] += score[j]
#         elif j in [5, 6, 7]:
#             test[agree] += score[j]

#     answer = []
#     for case in kakao_test:
#         max_score = max(test[c] for c in case)
#         for c in case:
#             if test[c] == max_score:
#                 answer.append(c)
#                 break

#     return "".join(answer)