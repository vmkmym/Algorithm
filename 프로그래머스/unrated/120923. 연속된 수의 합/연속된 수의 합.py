def solution(num, total):
    a = (2 * total // num + 1 - num) // 2
    answer = [a + i for i in range(num)]
    return answer
