def solution(elements):
    length = len(elements)
    sums = set()
    
    for i in range(length):
        sum = 0
        for j in range(length):
            sum += elements[(i + j) % length]
            sums.add(sum)
            
    return len(sums)

# 원형 수열 문제 풀기 위해 다음의 개념 이해하기
'''
원형 수열(Circular Sequence): 원형 수열은 마지막 요소와 첫 번째 요소가 연결된 수열입니다. 이는 마지막 요소 다음에 첫 번째 요소가 오는 것처럼 생각할 수 있습니다.

모듈로 연산(Modulo Operation): 원형 수열에서 인덱스를 계산할 때 모듈로 연산이 자주 사용됩니다. 이는 인덱스가 수열의 길이를 초과할 경우, 인덱스를 수열의 처음으로 돌리는 역할을 합니다.

부분 수열(Subsequence): 부분 수열은 수열에서 일부 원소를 선택하여 만든 수열입니다. 원형 수열에서 부분 수열을 선택할 때는 연속적인 원소를 선택하며, 선택 범위가 마지막 요소를 넘어 첫 번째 요소로 이어질 수 있습니다.

집합(Set): Python의 set은 중복을 허용하지 않는 컬렉션입니다. 이를 이용하면 중복 없이 합을 저장할 수 있습니다.
'''