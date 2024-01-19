def solution(word):
    weight = [sum(5**i for i in range(5-j)) for j in range(5)]
    alpha = {'A': 0, 'E': 1, 'I': 2, 'O': 3, 'U': 4}
    answer = 0

    for i in range(len(word)):
        answer += alpha[word[i]] * weight[i] + 1

    return answer

# 완전탐색문제지만 완전탐색은 비효율적이므로 가중치를 이용해서 풀었음
# 완전탐색은 product를 이용해서 풀었음
from itertools import product

def solution(word):
    alphabet = ['A', 'E', 'I', 'O', 'U']
    dictionary = []

    for i in range(1, 6):
        for combination in product(alphabet, repeat=i):
            dictionary.append(''.join(combination))

    dictionary.sort()
    return dictionary.index(word) + 1