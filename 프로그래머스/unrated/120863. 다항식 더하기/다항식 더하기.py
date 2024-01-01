def solution(polynomial):
    c = 0
    x = 0
    result = []
    
    for term in polynomial.split(" + "):
        if term.isnumeric():
            c += int(term)
        else:
            x += int(term[:-1] or "1")

    if x > 1:
        result.append(f"{x}x")
    elif x == 1:
        result.append("x")

    if c:
        result.append(str(c))

    return " + ".join(result)

# 이것도 다른 사람 풀이 참고해서 품


# 다른 사람 풀이
def solution(polynomial):
    xnum = 0
    const = 0
    
    for c in polynomial.split(' + '):
        if c.isdigit():
            const+=int(c)
        else:
            xnum = xnum+1 if c=='x' else xnum+int(c[:-1])
            
    if xnum == 0:
        return str(const)
    elif xnum==1:
        return 'x + '+str(const) if const!=0 else 'x'
    else:
        return f'{xnum}x + {const}' if const!=0 else f'{xnum}x'
