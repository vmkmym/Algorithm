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



'''
브루트포스 알고리즘은 가능한 모든 경우의 수를 탐색하여 문제를 해결하는 알고리즘입니다. 
브루트포스 알고리즘은 "무식한 힘"이라는 의미를 가지고 있으며, 주어진 문제에 대해 모든 가능한 조합을 시도하여 정확한 답을 찾는 방법입니다.

브루트포스 알고리즘은 다음과 같은 과정을 거칩니다:
1. 문제 공간 정의: 문제의 가능한 모든 해를 나타내는 공간을 정의합니다. 이는 문제의 변수와 범위에 따라 다를 수 있습니다.
2. 가능한 조합 생성: 문제 공간에서 가능한 모든 조합을 생성합니다. 이를 위해 반복문, 재귀 호출 등의 방법을 사용할 수 있습니다.
3. 조합 검사: 생성된 조합을 검사하여 문제의 조건을 만족하는지 확인합니다. 문제의 조건을 만족하는 조합이라면 결과를 저장하거나 출력합니다.
4. 모든 조합 확인: 모든 조합을 확인할 때까지 2단계와 3단계를 반복합니다.

브루트포스 알고리즘은 가능한 조합을 모두 확인하기 때문에 정확한 답을 찾을 수 있지만, 경우의 수가 많은 경우 시간과 공간 복잡도가 크게 증가할 수 있습니다. 
따라서 입력 크기가 작은 문제나 최적해를 찾을 필요가 없는 경우에 주로 사용됩니다.

브루트포스 알고리즘은 간단하고 직관적인 방법이지만, 효율성을 개선하기 위해 다른 알고리즘과 결합하여 사용하는 경우도 있습니다. 
예를 들어, 브루트포스 알고리즘으로 가능한 모든 조합을 생성한 후, 다이나믹 프로그래밍이나 그리디 알고리즘 등을 사용하여 중복 계산을 피하거나 최적해를 찾을 수 있습니다.
'''
