def solution(arr):
    answer = []
    for num in arr:
        if not answer or answer[-1] != num:
            answer.append(num)
    return answer

# 연속된 숫자에서 중복만 제거하고 순서를 유지하는건데, 문제 대충봐서 테스트 1 왜 통과를 못하지? 이러고 있었네