def solution(age):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    
    while age > 0:
        remainder = age % 10
        result = alphabet[remainder] + result
        age //= 10
    
    return result


# 다른 사람 풀이
def solution(age):
    age = str(age)
    age = age.replace("0", "a")
    age = age.replace("1", "b")
    age = age.replace("2", "c")
    age = age.replace("3", "d")
    age = age.replace("4", "e")
    age = age.replace("5", "f")
    age = age.replace("6", "g")
    age = age.replace("7", "h")
    age = age.replace("8", "i")
    age = age.replace("9", "j")
    return age

'''
chr() 함수는 주어진 숫자에 해당하는 ASCII 코드의 문자를 반환하는 파이썬 내장 함수입니다. 
ASCII(American Standard Code for Information Interchange)는 텍스트를 컴퓨터에서 처리하기 위해 사용되는 표준 문자 인코딩 방식 중 하나입니다.
'''
def solution(age):
    return ''.join([chr(int(i)+97) for i in str(age)])

# 딕셔너리
def solution(age):
    conv = {'0':'a','1':'b','2':'c','3':'d','4':'e'
            ,'5':'f','6':'g','7':'h','8':'i','9':'j'}
    return ''.join(conv[i] for i in str(age))

# `maketrans()` 함수는 문자열에서 변환 테이블을 생성하고, `translate()` 함수는 해당 변환 테이블을 사용하여 문자열의 문자를 변환합니다.
def solution(age):
    aa = str(age)
    return aa.translate(str.maketrans('0123456789', 'abcdefghij'))
