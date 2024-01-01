def solution(num, total):
    a = (2 * total // num + 1 - num) // 2
    answer = [a + i for i in range(num)]
    return answer

# 풀이 해석
# total은 연속된 숫자의 합, 연속된 숫자의 개수는 num.
# 우리는 연속된 숫자의 첫 항인 a를 등차수열의 합을 이용하여 찾아야 함
# 등차수열의 합 = (시작값 + 끝값) * 개수 / 2입니다.
# 따라서 (시작값 + 끝값) * 개수 / 2 = total 식을 변형하면, (시작값 + (시작값 + 개수 - 1)) * 개수 / 2 = total이 되고
# 이를 정리하면, 시작값 * 개수 + 개수 * (개수 - 1) / 2 = total이 됨
# 이것을 풀어서 시작값에 관한 수식으로 정리하면, 시작값 = (2 * total // num + 1 - num) // 2가 됨
