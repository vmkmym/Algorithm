def solution(num, n):
    if 2 <= num <= 100 and 2 <= n <= 9:
        return 1 if num % n == 0 else 0

# 고수들의 풀이
# num%n은 int 값이지만, 이를 not() 함수 안에 넣으면 int가 bool로 해석되어서 num%n이 0이면 False로, 0이 아니면 True로 해석
def solution(num, n):
    return int(not(num % n))
