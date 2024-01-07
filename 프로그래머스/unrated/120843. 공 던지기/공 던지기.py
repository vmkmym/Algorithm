def solution(numbers, k):
    return numbers[(k-1)*2 % len(numbers)]
# k번째 공을 던진 사람의 번호니까 k-1
# 한 명씩 건너뜀 *2
# 배열 사이즈로 나눈 인덱스