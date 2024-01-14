def solution(clothes):
    clothes_dict = {}
    answer = 1
    for _ , item in enumerate(clothes, start=1):
        clothes_dict[item[1]] = clothes_dict.get(item[1], 0) + 1
    for value in clothes_dict.values():
        answer *= (value + 1) # 해당 종류의 옷을 입는 경우의 수 + 입지 않는 경우(1)
    return answer - 1 # 모든 옷을 입지 않는 경우의 수 1을 빼준다.