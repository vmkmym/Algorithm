# 백준 1339번 단어수학
N = int(input())
words = [input().strip() for _ in range(N)]
        
def math_word(words):
    alpha = [0] * 26

    for word in words:
        i = 0
        for w in word[::-1]:
            alpha[ord(w) - ord('A')] += (10 ** i)
            i += 1

    alpha.sort(reverse=True)

    result = 0
    for i in range(9, 0, -1):
        result += i * alpha[9-i]

    return result

print(math_word(words))