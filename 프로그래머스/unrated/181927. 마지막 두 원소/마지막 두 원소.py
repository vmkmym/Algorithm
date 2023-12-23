def solution(num_list):
    if num_list[-1] > num_list[-2]:
        num_list.append(num_list[-1] - num_list[-2])
    else:
        num_list.append(num_list[-1] * 2)
        
    return num_list

# 4점 받음 삼항 연산자로 한 줄로 쓸 수 있었지만 너무 길어져서 가독성 떨어짐 
# 다른 사람 풀이도 대체로 비슷
