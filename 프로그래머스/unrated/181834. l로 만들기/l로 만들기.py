def solution(myString):
    target = 'abcdefghijk'
    
    for char in target:
        myString = myString.replace(char, 'l')
        
    return myString