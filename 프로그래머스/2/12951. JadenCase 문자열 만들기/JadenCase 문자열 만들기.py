# def solution(s):
#     jadenCase = ''
#     words = s.split()
    
#     for idx, word in enumerate(words):
#         if word[0].isdigit():
#             jadenCase += word.lower()
#         else:
#             jadenCase += word[0].upper() + word[1:].lower()
        
#         if idx != len(words) - 1:
#             jadenCase += ' '
    
#     return jadenCase

def solution(s):
    words = s.split(' ')
    answer = ''
    for i, word in enumerate(words):
        if word:
            words[i] = word[0].upper() + word[1:].lower()
        else:
            words[i] = ''

    for i in range(len(words)):
        answer += words[i]
        if i != len(words) - 1:
            answer += ' '
    return answer