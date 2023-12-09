a = int(input())
print(f"{a} is even" if 1 <= a <= 1000 and a % 2 == 0 else f"{a} is odd")


# 문자열 포맷팅을 통해서 짝수면 even 홀수면 odd를 출력
n = int(input())
print(f"{n} is {'even' if n % 2 == 0 else 'odd'}")
