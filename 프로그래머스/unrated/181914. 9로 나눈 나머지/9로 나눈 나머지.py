def solution(number):
    return sum(int(num) for num in str(number)) % 9

# 다른 사람 풀이
# 그냥 이렇게 해도 되는거였으면,,, 저렇게 안했지..
def solution(number):
    return int(number) % 9
