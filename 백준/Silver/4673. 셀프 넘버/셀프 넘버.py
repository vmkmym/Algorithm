# 셀프넘버가 없는 숫자를 구하는 문제
def self_number(number):
    total_num = number # total_num을 number로 초기화하는 이유는 number가 0이 될 때까지 반복문을 돌리기 위함
    while number != 0:
        total_num += number % 10 # 마지막 자리 수를 더함
        number //= 10 # number의 자릿수를 줄임
    return total_num

self_numbers = set(range(1, 10001)) # 셀프넘버 리스트
generated_numbers = set() # 생성자 숫자 리스트

for i in range(1, 10001):
    generated_numbers.add(self_number(i)) # 1부터 10000까지 생성자 숫자를 리스트에 추가

self_numbers = self_numbers - generated_numbers # 셀프 넘버가 있는 숫자 리스트

for num in sorted(self_numbers):
    print(num)

# Brute Force로 풀 수 있는 문제
# 브루트 포스란 가능한 모든 경우의 수를 일일이 확인하면서 문제를 해결하는 방식
# 1부터 10000까지의 모든 숫자에 대해 생성자를 찾아내는 과정