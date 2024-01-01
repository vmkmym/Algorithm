def solution(sides):
    sides.sort()
    return sum(1 for i in range(1, sum(sides)) if sides[1] < sides[0] + i)

# 다른 사람 풀이
# (max(sides) - (max(sides) + 1 - min(sides)) + 1) + (sum(sides) - max(sides) - 1)
# n이 가장 길지 않은 경우의 조건 max(sides) < min(sides) + n 과 
# n이 가장 긴 조건인 sum(sides) > n 을 둘다 만족하는 n의 개수를 찾으면 아래와 같은 결과가 나온다
def solution(sides):
    return sum(sides) - max(sides) + min(sides) - 1

# 다른 사람 풀이 : 레전드
# sum - max + min - 1인데, 배열의 원소는 2개 이고 사실상 합에서 최댓값을 뺀 값이 최솟값이므로 최솟값의 2배 - 1도 가능
# a-b+1 <= x <= a+b-1 
def solution(sides):
    return 2 * min(sides) - 1

# 다른 사람 풀이
def solution(sides):
    sides.sort()
    L1 = len([i for i in range(1,sides[1]) if i+sides[0]>sides[1]])
    L2 = len([i for i in range(sides[1],sides[0]+sides[1])])
    return L1+L2
