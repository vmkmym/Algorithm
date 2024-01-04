def solution(my_string):
    counts = [0] * 52 
    
    for char in my_string:
        if 'A' <= char <= 'Z':
            counts[ord(char) - ord('A')] += 1 
        elif 'a' <= char <= 'z':
            counts[ord(char) - ord('a') + 26] += 1 
    
    return counts

# 아스키 코드 이용한 풀이
# ord() 함수를 사용하여 각 알파벳을 숫자로 변환한 후, 해당 숫자를 리스트의 인덱스로 활용하여 알파벳의 개수를 증가
def solution(my_string):
    answer = [0] * 52  
    
    for x in my_string: 
        if x.isupper():  
            answer[ord(x) - 65] += 1  
        else:  
            answer[ord(x) - 71] += 1  
    
    return answer  

# 카운트
def solution(my_string):
    return [my_string.count(alphabet) for alphabet in 'abcdefghijklmnopqrstuvwxyz'.upper()+'abcdefghijklmnopqrstuvwxyz']

# string 모듈
import string

def solution(my_string):
    # 대소문자 알파벳을 키로 갖고, 초기값을 0으로 갖는 딕셔너리를 생성합니다.
    count = dict.fromkeys(string.ascii_uppercase + string.ascii_lowercase, 0)
    
    # 입력된 문자열을 순회하면서 각 문자의 개수를 세어 딕셔너리에 저장합니다.
    for s in my_string:
        count[s] += 1
    
    # 딕셔너리의 값들을 리스트로 변환하여 반환합니다.
    return list(count.values())