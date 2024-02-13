def solution(numbers):
    if len(numbers) < 2:
        return "Error: 주어진 정수배열의 길이가 2보다 작습니다."
    
    firstNum, secondNum = float('-inf'), float('-inf')
    
    for num in numbers:
        if num > firstNum:
            firstNum, secondNum = num, firstNum
        elif num < firstNum and num > secondNum:
            secondNum = num
            
    return secondNum if secondNum != float('-inf') else "Error: 두 번째로 큰 수가 존재하지 않습니다."

def test_solution():
    # 테스트 케이스
    assert solution([5,1,52,57,13,53]) == 53
    # 모든 원소가 같은 경우
    assert solution([5, 5, 5, 5, 5]) == "Error: 두 번째로 큰 수가 존재하지 않습니다."
    # 원소가 하나인 경우
    assert solution([1]) == "Error: 주어진 정수배열의 길이가 2보다 작습니다."
    # 원소가 두 개인 경우
    assert solution([3, 3, 2, 2, 1, 1]) == 2
    # 음수만 존재하는 경우
    assert solution([-1, -2, -3, -4, -5]) == -2
    # 음수와 양수가 섞여 있는 경우
    assert solution([-1, 2, -3, 4, -5]) == 2
    print("All test cases passed")
    
test_solution()