string = input()

stack = []
depth_result = [0] * 50
depth = 0

for ch in string:
    if ch != ")":
        if ch == "(":
            depth += 1
            depth_result[depth] = 0
        stack += [ch]
    else:
        for i in range(len(stack) - 1, -1, -1):
            if stack[i] == "(":
                num = depth_result[depth]
                for j in stack[i + 1 :]:
                    num += 1
                depth -= 1
                depth_result[depth] += num * int(stack[i - 1])
                del stack[i - 1 :]

                break
print(depth_result[0] + len(stack))