n = input()
number = 0
idx = 0 

while True:
    number += 1 # 주어진 수의 현재 인덱스가 현재 수랑 일치하지 않으면 숫자를 늘린다
    for num in str(number): 
        if n[idx] == num: # 만약 주어진 수의 현재 인덱스가 현재 수랑 일치하면
            idx += 1 # 인덱스 증가
            if idx >= len(n): # 인덱스가 주어진 수의 길이보다 크거나 같으면
                print(number) # 해당 수를 출력
                break # 모든 반복문을 빠져나온다
    else: # 만약 주어진 수의 현재 인덱스가 현재 수랑 일치하지 않으면
        continue # while문으로 돌아가 다음 수를 검사
    break

# 234092를 예로 들어보자
# 1. number = 0, idx = 0
# 2. number = 1, idx = 0, n[idx] = 2, num = 1, 1 != 2, continue
# 3. number = 2, idx = 0, n[idx] = 2, num = 2, 2 == 2, idx = 1
# 4. number = 3, idx = 1, n[idx] = 3, num = 3, 3 == 3, idx = 2
# 5. number = 4, idx = 2, n[idx] = 4, num = 4, 4 == 4, idx = 3
# 6. number = 5, idx = 3, n[idx] = 0, num = 5, 5 != 0, continue
# 이런 식으로 진행되다가 idx가 n의 길이보다 커지면 해당 수를 출력하고 반복문을 빠져나온다