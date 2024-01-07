def solution(bin1, bin2):
    sum_decimal = int(bin1, 2) + int(bin2, 2)
    return bin(sum_decimal)[2:]