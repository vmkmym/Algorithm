def solution(n):
    answer = []
    i = 2
    while i <= n:
        if n % i == 0:
            answer.append(i)
            n /= i
        else:
            i += 1

    return sorted(list(set(answer)))


# 앱과정 때 풀었었나 왜 .. 소인수분해 익숙하지
# answer를 list로 선언했지만 set()으로 중복을 제거하면서 다시 list로 선언해줘야하고, set은 순서를 간과하므로 sorted로 정렬해줘야 함
# 풀면서 테스트 케이스 4개가 통과가 안되서 힌트보고 품

# 다른 사람 풀이 : 에라토스테네스의 체

에라토스테네스의 체 동작원리

1. 2부터 시작하여 찾고자 하는 범위의 모든 수를 포함하는 배열을 생성합니다.
2. 2부터 시작하여 배열에서 가장 작은 수를 찾습니다. 이것은 소수입니다.
3. 찾은 소수의 배수들을 모두 지웁니다. (소수의 배수들은 소수가 아니므로)
4. 지워지지 않은 다음으로 남은 수를 찾아 해당 수를 소수로 선택하고, 해당 소수의 배수들을 지웁니다.
5. 이 과정을 반복하면서 지워지지 않은 모든 수를 소수로 선택합니다.

이 알고리즘을 사용하면 주어진 범위 내의 모든 소수를 효율적으로 찾을 수 있습니다. 
알고리즘의 핵심은 지워지지 않은 수들은 모두 소수라는 것입니다. 
따라서 소수를 찾고자 하는 범위의 제곱근까지만 반복하여 계산하면 됩니다.

import math
from itertools import permutations

def is_prime(n):
    if n < 2:
        return False
    if n in [2, 3, 5, 7]:
        return True

    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


def solution(n):
    primes = list(filter(lambda n: is_prime(n), range(1, n+1)))

    answer = []
    while n != 1:
        for prime in primes:
            if n % prime == 0:
                n //= prime
                if prime not in answer:
                    answer.append(prime)

    return answer