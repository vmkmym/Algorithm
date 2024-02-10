from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([0] * bridge_length)
    trucks = deque(truck_weights)
    time = 0
    bridge_weight = 0 # 다리 위 트럭 무게

    while trucks:
        time += 1
        bridge_weight -= bridge.popleft() # 다리 위 트럭 무게 -= 다리를 지나는 트럭 무게

        if bridge_weight + trucks[0] <= weight: # 다리에 트럭이 올라갈 수 있으면
            truck = trucks.popleft() 
            bridge.append(truck) # 다리에 트럭을 올린다.
            bridge_weight += truck # 다리 무게에 트럭 무게를 더해준다.
        else:
            bridge.append(0)

    return time + bridge_length # 마지막 트럭이 다리를 건너는 시간 == bridge_length초 걸림