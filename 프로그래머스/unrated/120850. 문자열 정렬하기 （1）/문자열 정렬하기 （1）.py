def solution(my_string):
    return [int(char) for char in sorted(my_string) if char.isdigit()]