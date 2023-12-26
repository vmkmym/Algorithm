def solution(intStrs, k, s, l):
    return [int(part[s:s + l]) for part in intStrs if int(part[s:s + l]) > k]

# for문에 if문 작성했는데 리스트 컴프리헨션 쓰고 싶어서 이렇게 바꿈
# 근데 점수 별로 안 높네.. 어떤 코드가 높은 점수 받았는지도 풀이에 나왔으면 좋을텐데..
