def solution(a, d, included):
    return sum(a + d * i  for i in range(len(included)) if included[i])


# 다른 사람의 풀이 해석
# enumerate() 함수는 배열의 각 요소와 인덱스를 순회하면서 튜플 형태로 반환
# enumerate(included)는 (i, f) 형태의 튜플을 반환하는데, i는 인덱스를, f는 해당 인덱스의 요소
# if f 부분은 f가 True인 경우에만 값을 계산하여 합산하는 조건
def solution(a, d, included):
    return sum(a + i * d for i, f in enumerate(included) if f)
