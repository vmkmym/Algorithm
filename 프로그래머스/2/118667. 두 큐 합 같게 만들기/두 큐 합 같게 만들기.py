from collections import deque

def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    sum1, sum2 = sum(queue1), sum(queue2)
    total_len = len(queue1)*3
    
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