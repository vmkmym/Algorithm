def int_range(a, b):
    if -100000 <= a <= 100000 and -100000 <= b <= 100000:
        return True
    else:
        return False
    
a, b = map(int, input().strip().split(' '))

if int_range(a, b):
    print(f"a = {a}")
    print(f"b = {b}")

