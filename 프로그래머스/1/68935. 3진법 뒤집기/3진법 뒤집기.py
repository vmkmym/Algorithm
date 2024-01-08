def solution(n):
    ternary = ''
    while n > 0:
        n, remainder = divmod(n, 3)
        ternary += str(remainder)
    
    decimal = 0
    for idx, digit in enumerate(ternary[::-1]):
        decimal += int(digit) * (3 ** idx)
    
    return decimal

# gpt 복붙.. 하지만 3진법 이해가 안간다..