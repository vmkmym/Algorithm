# 백준 1339번 단어수학
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
        result += values[i] * (9 - i) # 119, 118
    return result # 119 + 118 = 187

# 백준 제출용 코드
# N = int(input())
# words = [input().strip() for _ in range(N)]
# print(math_word(words))

# 테스트 코드
def test_math_word():
    assert math_word(["AAA", "AAA"]) == 1998
    assert math_word(["GCF", "ACDEB"]) == 99437
    assert math_word(list("ABCDEFGHIJ")) == 45
    assert math_word(["AB", "BA"]) == 187
    print("All test cases passed!")

test_math_word()


# 알파벳의 가중치를 저장할 리스트
weights = [0] * 99

# 단어의 개수를 입력받음
for _ in range(int(input())):
    # 각 단어를 거꾸로 처리
    for char in input()[::-1]:
        # 각 알파벳의 가중치를 계산
        weights[ord(char)] -= _
        _ *= 10

# 가중치를 오름차순으로 정렬
weights.sort()

# 가장 높은 가중치를 가진 알파벳부터 가장 높은 숫자를 할당하고 합계를 계산
print(sum(weight * value for weight, value in zip(weights, range(-9, 0))))