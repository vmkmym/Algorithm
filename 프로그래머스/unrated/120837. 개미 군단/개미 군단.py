def solution(hp):
    ants = [5, 3, 1]
    count = 0

    for ant in ants:
        count += hp // ant
        hp %= ant

    return count

# compound assignment operators 복합 할당 연산자 유용하다
x = 10

x += 1    # add 1 to x
x -= 1    # subtract 1 from x
x *= 10   # mulitply x by 10
x /= 2    # divide x by 2

x //= 3   # floor divide x by 3
x %= 10   # modulus x by 10
x **= 2   # square x


# 다른 사람 풀이
def solution(hp):    
    return hp // 5 + (hp % 5 // 3) + ((hp % 5) % 3)
