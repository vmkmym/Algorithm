import sys
input = sys.stdin.read
output = sys.stdout.write

def main():
	digit = [False] * 10
	cnt = 0
	N, K = input().split()
	K = int(K)

	if K == 10:
		print("1023456789")
	elif K == 9:
		print("102345678")
	else:
		while cnt != K:
			digit = [False] * 10
			cnt = 0
			N = str(int(N) + 1)
			for char in N:
				digit[int(char)] = True
			cnt = sum(digit)
		print(N)

if __name__ == "__main__":
	main()