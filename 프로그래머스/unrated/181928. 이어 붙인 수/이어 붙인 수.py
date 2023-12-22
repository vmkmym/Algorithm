def solution(num_list):
    odd = int(''.join(str(num) for num in num_list if num % 2 != 0))
    even =  int(''.join(str(num) for num in num_list if num % 2 == 0))
    return odd+even