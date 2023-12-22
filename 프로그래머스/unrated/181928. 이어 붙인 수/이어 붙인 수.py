def solution(num_list):
    odd = int(''.join(str(num) for num in num_list if num % 2 != 0))
    even =  int(''.join(str(num) for num in num_list if num % 2 == 0))
    return odd+even

# 나랑 거의 비슷하게 푼 풀이도 있음
# 선형 시간복잡도가 최선인 것 같은데 리스트의 크기가 매우 크면 성능 떨어짐
# 시간복잡도가 리스트의 길이에 비례하기 때문
