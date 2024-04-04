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
                break
    else:
        continue
    break