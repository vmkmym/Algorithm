def solution(arr):
    row_len = len(arr)
    col_len = len(arr[0])
    
    if row_len == col_len:
        return arr
    elif row_len > col_len:
        for i in range(row_len):
            diff = row_len - col_len
            arr[i].extend([0] * diff)
    else:
        for i in range(row_len, col_len):
            arr.append([0] * col_len)
    
    return arr

            