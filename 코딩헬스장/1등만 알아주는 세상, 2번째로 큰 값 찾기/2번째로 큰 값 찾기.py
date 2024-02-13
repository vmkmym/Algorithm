def solution(numbers):
    firstNum, secondNum = float('-inf'), float('-inf')
    for num in set(numbers):
        if num > firstNum:
            firstNum, secondNum = num, firstNum
        elif num > secondNum:
            secondNum = num
    return secondNum

def test_solution():
    # 테스트 케이스
    assert solution([5,1,52,57,13,53]) == 53
    # 모든 원소가 같은 경우
    assert solution([5, 5, 5, 5, 5]) == 5 
    # 원소가 하나인 경우
    assert solution([1]) == float('-inf')
    # 원소가 두 개인 경우
    assert solution([3, 3, 2, 2, 1, 1]) == 2
    # 음수만 존재하는 경우
    assert solution([-1, -2, -3, -4, -5]) == -2
    # 음수와 양수가 섞여 있는 경우
    assert solution([-1, 2, -3, 4, -5]) == 2
    print("All test cases passed")
    
test_solution()