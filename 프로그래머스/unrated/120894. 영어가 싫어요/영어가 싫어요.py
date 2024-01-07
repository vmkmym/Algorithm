def solution(numbers):
    dic = {
        "zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
        "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"
    }
    
    result = ''
    word = ''
    
    for char in numbers:
        word += char
        if word in dic:
            result += dic[word]
            word = ''
        
    return int(result)

# 아 왜 enumerate, replace 생각을 못했지
# 다른 사람 풀이 
def solution(numbers):
    for num, eng in enumerate(["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
        numbers = numbers.replace(eng, str(num))
    return int(numbers)