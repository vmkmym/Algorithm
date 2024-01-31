def solution(s, skip, index):
    alphabet = [chr(i) for i in range(ord('a'), ord('z')+1) if chr(i) not in skip]
    cipher_text = ''
    for char in s:
        char_index = (alphabet.index(char) + index) % len(alphabet)
        cipher_text += alphabet[char_index]
    return cipher_text