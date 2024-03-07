# 문자를 입력받으면 아스키코드 10진수 int로 전환하고 0~127 사이의 int 값을 입력받으면 아스키코드에 해당하는 문자로 전환하는 함수를 작성하세요.
# TypeError: ord() expected a character, but string of length 2 found -> len(i) == 1

def ascii_code(i):
    if isinstance(i, str) and len(i) == 1:
        return ord(i)
    elif isinstance(i, int) and 0 <= i <= 127:
        return chr(i)
    else:
        return "error: invalid input."

# Test
import unittest

class TestAsciiCode(unittest.TestCase):
    def test_char_to_ascii(self):
        self.assertEqual(ascii_code('A'), 65)
        self.assertEqual(ascii_code('a'), 97)
        self.assertEqual(ascii_code('4'), 52)

    def test_ascii_to_char(self):
        self.assertEqual(ascii_code(65), 'A')
        self.assertEqual(ascii_code(97), 'a')
        self.assertEqual(ascii_code(48), '0')

    def test_invalid_input(self):
        self.assertEqual(ascii_code('AB'), "error: invalid input.")
        self.assertEqual(ascii_code(128), "error: invalid input.")
        self.assertEqual(ascii_code(-1), "error: invalid input.")

if __name__ == '__main__':
    unittest.main()