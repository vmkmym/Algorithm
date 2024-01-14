def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)): # arr1의 행
        answer.append([]) # answer에 행 추가
        for j in range(len(arr2[0])): # arr2의 열
            answer[i].append(0) # answer에 열 추가
            for k in range(len(arr1[0])): # arr1의 열
                answer[i][j] += arr1[i][k] * arr2[k][j] # 행렬의 곱
    return answer