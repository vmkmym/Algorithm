import time
import random
from typing import List

# 리스트 컴프리헤션을 사용한 퀵 정렬 (배열을 3번 순회)
def quick_sort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# 배열을 1번 순회하는 방식으로 리스트 분할
def quick_sort2(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2] 
    left, right, middle = [], [], []
    for i in arr:
        if i < pivot:
            left.append(i)
        elif i == pivot:
            middle.append(i)
        else:
            right.append(i)
    return quick_sort2(left) + middle + quick_sort2(right)


def test_sort_functions():
    arr = [random.randint(0, 1000) for _ in range(10000)]

    start = time.time()
    quick_sort(arr.copy())  # quick_sort 함수 테스트
    end = time.time()
    print(f"quick_sort took {end - start} seconds.")

    start = time.time()
    quick_sort2(arr.copy())  # quick_sort2 함수 테스트
    end = time.time()
    print(f"quick_sort2 took {end - start} seconds.")
    
    start = time.time()
    arr.sort()  # 파이썬 내장 정렬 함수 테스트
    end = time.time()
    print(f"Team sort took {end - start} seconds.")

test_sort_functions()
# 실행결과 quick_sort2가 더 빠른 것 확인함
    # quick_sort took 0.011791229248046875 seconds.
    # quick_sort2 took 0.009579896926879883 seconds.
    # team sort took 0.0012738704681396484 seconds.


# 궁금증 1. quick_sort2 함수는 quick_sort 함수보다 더 빠른가?
    # 리스트 분할 방식이 다름
    # quick_sort 함수는 리스트 컴프리헨션을 사용하여 리스트를 분할함(배열을 3번 순회)
    # quick_sort2 함수는 for문을 사용하여 리스트를 분할함(배열을 1번 순회)
    # 테스트 해보니 더 빠르다는 것을 확인함

# 궁금증 2. 파이썬 내장 함수에도 정렬 함수가 있는데 퀵 정렬과 비교했을 때의 시간복잡도 차이는?
    # 파이썬의 내장 정렬 함수인 sort()와 sorted()는 팀소트(Timsort)라는 알고리즘을 사용함.
    # 팀소트는 최악의 경우에도 O(nlogn)의 시간복잡도를 보장함.
    # 퀵정렬은 최악의 경우에 O(n^2)의 시간복잡도를 가짐.
    # 그러나 퀵 정렬은 이미 부분적으로 정렬되어 있거나 동일한 값이 많이 포함된 경우 등의 특정 상황에서는 더 빠른 성능을 보임
    # 또한, 퀵 정렬은 제자리 정렬(in-place sort)이 가능하므로, 추가적인 메모리를 거의 사용하지 않음
    
# 궁금증 3. 파이썬이 팀소트를 사용하는 이유는 무엇인가?
    # 실제 데이터에 대해 매우 효울적이기 때문
    # 팀소트는 퀵정렬과 병합정렬의 장점을 조합한 알고리즘
    # 적응성: 팀소트는 데이터가 이미 부분적으로 정렬되어 있는 경우 이를 인식하고, 이에 따라 정렬 과정을 최적화.
    # 안정성: 팀소트는 안정적인 정렬 알고리즘으로, 동일한 값에 대해 원래의 순서를 유지함.
    # 최악의 경우에도 O(nlogn)의 시간복잡도를 보장함.
    # 메모리 효율성: 팀소트는 추가적인 메모리를 적게 사용함.
    
# 궁금증 4. 팀소트 자체가 퀵정렬과 병합정렬의 장점을 조합한거면 퀵정렬보다 좋다고 할 수 있는가?
    # 상황에 따라 다름
    # 주어진 문제의 특성과 요구 사항에 따라 달라짐.
    # 일반적으로 파이썬의 내장 정렬 함수인 sort()와 sorted()를 사용하는 것이 가장 좋은 선택일 수 있으나 특정 상황에서는 아닐 수 있음