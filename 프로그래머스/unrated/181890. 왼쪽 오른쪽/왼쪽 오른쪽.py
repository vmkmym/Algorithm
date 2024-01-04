def solution(str_list):
    left_index = -1 if 'l' not in str_list else str_list.index('l')
    right_index = -1 if 'r' not in str_list else str_list.index('r')

    if left_index >= 0 and right_index >= 0:
        if left_index < right_index:
            return str_list[:left_index]
        else:
            return str_list[right_index + 1:]
    elif left_index >= 0:
        return str_list[:left_index]
    elif right_index >= 0:
        return str_list[right_index + 1:]
    else:
        return []
