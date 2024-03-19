from collections import Counter

def math_word(words):
    counter = Counter()
    
    # 각 단어의 알파벳별 가중치를 계산 
    # (가중치는 10의 자리수로 계산한다. ex) AB = 10A + B, BA = 10B + A
    for word in words:
        length = len(word)
        for i in range(length):
            counter[word[i]] += 10 ** (length - i - 1)

    # 가중치를 기준으로 내림차순 정렬. ex) [10+1 = 11, 1+10 =11]
    values = sorted(counter.values(), reverse=True)
    
    # 가중치가 높은 순으로 9부터 곱해서 더한다.
    result = 0
    for i in range(len(values)):
        result += values[i] * (9 - i) # 11*9, 11*8
    return result # 119 + 118 = 187

N = int(input())
words = [input().strip() for _ in range(N)]
print(math_word(words))

# 테스트 코드
def test_math_word():
    assert math_word(["AAA", "AAA"]) == 1998
    assert math_word(["GCF", "ACDEB"]) == 99437
    assert math_word(list("ABCDEFGHIJ")) == 45
    assert math_word(["AB", "BA"]) == 187
    print("All test cases passed!")

test_math_word()