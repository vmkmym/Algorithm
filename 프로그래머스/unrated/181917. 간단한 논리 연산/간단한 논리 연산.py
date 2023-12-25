def solution(x1, x2, x3, x4):
    return (x1 or x2) and (x3 or x4)

# 다른 풀이
# or과 and를 기억하자
def solution(x1, x2, x3, x4):
    return (x1 | x2) & (x3 | x4)

# 람다(lambda) 함수는 익명 함수로, def 키워드를 사용하지 않고도 작성할 수 있는 간단한 형태의 함수이다
# 람다 함수는 보통 한 줄로 간단한 연산을 수행하거나, 함수를 매개변수로 전달해야 하는 경우 등에 활용한다
# lambda 매개변수들: 표현식
solution = lambda w, x, y, z : (w or x) and (y or z)
