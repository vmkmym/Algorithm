def zoo(n):
    a = b = c = 1
    for _ in range(n-1):
        a, b, c = (a+b+c)%9901, (a+c)%9901, (a+b)%9901
    return (a+b+c)%9901

try:
    print(zoo(int(input())))
except:
    print("Invalid input. Please enter a non-negative integer.")