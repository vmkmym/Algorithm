def solution(numlist, n):
    return sorted(numlist, key = lambda i: (abs(i - n), -i))

# 정수 리스트를 받아서 n과의 거리 비교 : 각 요소에서 n 뺀 절댓값, 거리가 같은 경우 음의 값으로 크기 비교 후 정렬
[sorted(), key 매개변수 : 정렬 기준](https://github.com/vmkmym/Algorithm/tree/main/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4/unrated/181921.%E2%80%85%EB%B0%B0%EC%97%B4%E2%80%85%EB%A7%8C%EB%93%A4%EA%B8%B0%E2%80%852)
