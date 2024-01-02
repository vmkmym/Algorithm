def solution(my_string):
    gather = ["a", "e", "i", "o", "u"]
    
    for char in gather:
        my_string = my_string.replace(char, '')
    
    return my_string