def solution(word):
    weight = [sum(5**i for i in range(5-j)) for j in range(5)]
    alpha = {'A': 0, 'E': 1, 'I': 2, 'O': 3, 'U': 4}
    answer = 0

    for i in range(len(word)):
        answer += alpha[word[i]] * weight[i] + 1

    return answer