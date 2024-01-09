n = int(input())


def movie_director(n):
    count = 0
    num = 666

    while True:
        if '666' in str(num):
            count += 1

        if count == n:
            return num

        num += 1


result = movie_director(n)
print(result)