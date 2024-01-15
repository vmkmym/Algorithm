def solution(numbers, target):
    def dfs(idx, result): # result: 방법의 수 저장
        if idx == len(numbers): # 재귀함수의 종료조건
            return 1 if result == target else 0
        else:
            return dfs(idx+1, result+numbers[idx]) + dfs(idx+1, result-numbers[idx])

    return dfs(0, 0)