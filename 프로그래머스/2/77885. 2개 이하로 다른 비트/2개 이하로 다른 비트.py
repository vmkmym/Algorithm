def solution(numbers):
    answer = []
    for i in numbers:
        # 짝수면 1을 더하고 결과 반환
        num = i
        cnt = 0
        # 홀수면 2로 나누고 나눈 횟수를 세서 2의 몇승을 더할지 결정
        while i % 2 == 1:
            cnt += 1
            i //= 2
        answer.append(num + 2**(cnt - 1) if cnt != 0 else num + 1) # 7 + 2^2 = 11
    return answer