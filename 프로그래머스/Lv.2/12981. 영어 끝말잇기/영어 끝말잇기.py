def solution(n, words):
    answer = []
    for i, word in enumerate(words):
        if word not in answer and (not answer or answer[-1][-1] == word[0]):
            answer.append(word)
        else:
            return [(i % n) + 1, (i // n) + 1]
    return [0, 0]
