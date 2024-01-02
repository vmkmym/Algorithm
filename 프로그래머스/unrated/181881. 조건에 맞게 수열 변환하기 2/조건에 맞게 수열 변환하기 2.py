def solution(arr):
    count = 0
    while True:
        new_arr = []
        
        for i in arr:
            if i >= 50 and i % 2 == 0:
                new_arr.append(i // 2)
            elif i < 50 and i % 2 != 0: 
                new_arr.append(i * 2 + 1)
            else:
                new_arr.append(i)
        
        count += 1
        
        if arr == new_arr:
            return count-1
        
        arr = new_arr
