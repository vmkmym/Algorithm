from collections import OrderedDict

def solution(my_string):
    return ''.join(OrderedDict.fromkeys(my_string))

# 입력된 순서를 유지하면서 중복을 제거하는 collections의 OrderedDict.fromkeys

