import re

def solution(files):
    def split_file(filename):
        match = re.match(r"([a-z\s\.-]*)(\d{1,5})(.*)", filename, re.I)
        if match:
            head, number, tail = match.groups()
            return head, number, tail
        else:
            return None
    
    return sorted(files, key=lambda f: (split_file(f)[0].lower(), int(split_file(f)[1])))