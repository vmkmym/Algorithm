from collections import defaultdict
import math

def solution(fees, records):
    in_time = defaultdict(int)
    total_time = defaultdict(int)
    
    # 출차한 차량일 경우
    for record in records:
        time, car_num, status = record.split()
        time = int(time.split(':')[0])*60 + int(time.split(':')[1])
        if status == 'IN':
            in_time[car_num] = time
        else:
            total_time[car_num] += time - in_time[car_num]
            del in_time[car_num]
    
    # 출차하지 않은 차량일 경우
    for car_num in in_time:
        total_time[car_num] += 1439 - in_time[car_num]
        
    answer = []
    
    # 주차요금
    for car_num, time in sorted(total_time.items()):
        fee = fees[1] if time <= fees[0] else fees[1] + math.ceil((time-fees[0])/fees[2])*fees[3]
        answer.append(fee)
    return answer