def solution(num_list):
    count = 0
    for num in num_list:
        while num != 1:
            if num % 2 == 0:
                num //= 2
            else:
                num = (num - 1) // 2
            count += 1
    return count

# 다른 사람 풀이 : 2진수로 비트수 계산하는 방식
'''
num_list에 있는 각 정수를 2진수로 변환한 후, 해당 2진수의 비트 수에서 3을 뺀 값을 모두 더하는 방식
bin() 함수는 주어진 정수를 2진수 문자열로 변환합니다. 
반환된 문자열은 0b로 시작하므로, 실제 비트 수를 나타내기 위해 len(bin(i)) - 3으로 각 정수의 2진수 비트 수를 계산합니다. -3을 하는 이유는 bin() 함수에 의해 반환된 문자열이 0b로 시작되기 때문에 이 두 자리를 제외하기 위함입니다.
'''
def solution(num_list):
    return sum(len(bin(i)) - 3 for i in num_list)
