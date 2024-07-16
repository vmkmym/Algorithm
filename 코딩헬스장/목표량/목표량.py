# 정답 코드

# 문자열은 수정이 불가능하므로 리스트로 변환
s = list(input())

# 뒤에서부터 탐색하며 오름차순이 깨지는 지점을 찾음
for i in range(len(s) - 2, -1, -1):
    if s[i] < s[i + 1]:
        break
else:
    print(0)
    exit()
    
# 오름차순이 깨지는 지점을 기준으로 뒤에서부터 탐색하며 교환할 위치를 찾음
for j in range(len(s) - 1, i, -1):
    if s[j] > s[i]:
        break
s[i], s[j] = s[j], s[i] # Swap
s[i + 1 :] = s[:i:-1] # i 이후의 문자열을 뒤집음

# 리스트를 문자열로 변환하여 출력
print("".join(s))

# 제출했던 코드는 permutation을 사용하여 모든 경우의 수를 탐색하였으나, 이 코드는 더 효율적으로 탐색함