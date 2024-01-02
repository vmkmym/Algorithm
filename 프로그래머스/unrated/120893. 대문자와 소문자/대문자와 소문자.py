def solution(my_string):
    new_str = ''
    
    for char in my_string:
        if char.islower():
            new_str += char.upper()
        elif char.isupper():
            new_str += char.lower()
        else:
            new_str += char

    return new_str
