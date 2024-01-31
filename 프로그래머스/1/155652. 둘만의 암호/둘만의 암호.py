def solution(s, skip, index):
    alphabet = [chr(i) for i in range(ord('a'), ord('z')+1) if chr(i) not in skip]
    cipher_text = ''.join([alphabet[(alphabet.index(char) + index) % len(alphabet)] for char in s])
    return cipher_text