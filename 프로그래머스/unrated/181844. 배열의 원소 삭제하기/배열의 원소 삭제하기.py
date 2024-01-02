def solution(arr, delete_list):
    return [new_arr for new_arr in arr if new_arr not in delete_list]