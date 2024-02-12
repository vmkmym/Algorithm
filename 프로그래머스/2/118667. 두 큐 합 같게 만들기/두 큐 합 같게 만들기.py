from collections import deque

def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    sum1, sum2 = sum(queue1), sum(queue2)
    total_len = len(queue1) * 3
    
    # 두 큐의 총 합이 홀수인 경우 -1을 반환
    if (sum1 + sum2) % 2 != 0:
        return -1
    
    count = 0
    while sum1 != sum2: # 두 큐의 합이 같아질 때 까지
        if sum1 < sum2: # 연산 횟수 줄이기 위해 큐 교환
            queue1, queue2 = queue2, queue1
            sum1, sum2 = sum2, sum1
        pop_val = queue1.popleft()
        sum1 -= pop_val
        queue2.append(pop_val)
        sum2 += pop_val
        count += 1
        
        # 연산 횟수가 두 큐의 길이의 합보다 큰 경우 -1을 반환
        if count > total_len:
            return -1

    return count

# 다른 사람의 풀이
def solution(queue1, queue2):
    indicator2 = sum(queue1) - int(sum(queue1+queue2)/2) # 큐의 합의 차이
    answer = 0 # 연산 횟수
    sub_list = (queue1+queue2+queue1)[::-1] # 이 리스트에서 원소를 빼면 queue1의 합이 줄어듦
    add_list = (queue2+queue1+queue2)[::-1] # 이 리스트에서 원소를 더하면 queue1의 합이 늘어남
    while indicator2 != 0:
        try: 
            if indicator2 > 0: # 큐 합의 차이가 양수인 경우
                indicator2 -= sub_list.pop() # 원소를 빼서 큐1의 합을 줄임
            else:
                indicator2 += add_list.pop() # 원소를 더해서 큐1의 합을 늘림
        except: 
            return -1
        answer += 1
    return answer

'''
Python의 int 타입은 메모리가 허용하는 한 어떤 크기의 정수도 저장할 수 있으므로, 이 문제에서는 오버플로우를 걱정할 필요가 없습니다.
그러나, 큐의 길이가 매우 크므로, sum(queue1)과 같은 연산을 반복적으로 수행하는 것은 비효율적입니다. 
이를 개선하기 위해, 각 큐의 합을 변수에 저장하고, 원소를 옮길 때마다 이 변수를 업데이트하는 방식을 사용하겠습니다.
'''