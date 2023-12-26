def solution(number):
    return sum(int(num) for num in str(number)) % 9
