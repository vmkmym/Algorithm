def solution(n, words):
    answer = [words[0]]
    
    for i, word in enumerate(words[1:], 1):
        if word in answer or answer[-1][-1] != word[0]:
            return [(i % n) + 1, (i // n) + 1]
        answer.append(word)
        
    return [0, 0]