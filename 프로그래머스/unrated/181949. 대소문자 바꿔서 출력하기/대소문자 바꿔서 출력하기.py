str = input()

if 1 <= len(str) <= 20:
    convert_str = "".join([char.upper() if char.islower() else char.lower() for char in str])
    print(convert_str)
