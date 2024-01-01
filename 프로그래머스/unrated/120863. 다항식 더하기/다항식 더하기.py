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

    