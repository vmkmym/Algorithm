def solution(my_string, is_suffix):
    suffixes = sorted([my_string[i:] for i in range(len(my_string))])
    return 1 if is_suffix in suffixes else 0

# 다른 사람 풀이
def solution(my_string, is_suffix):
    return int(my_string.endswith(is_suffix))

# endswith()
endswith()는 문자열이 특정 접미사(suffix)로 끝나는지 여부를 확인하는 문자열 메서드입니다. 
문자열이 지정된 접미사로 끝날 경우 True를 반환하고, 그렇지 않으면 False를 반환합니다.
문자열 끝 부분에 특정 접미사가 있는지를 확인합니다. 
기본적으로 하나 또는 여러 개의 접미사를 지정할 수 있습니다.
