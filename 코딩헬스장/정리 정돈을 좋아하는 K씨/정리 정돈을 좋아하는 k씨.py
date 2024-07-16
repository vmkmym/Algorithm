# 정답코드
def main():
	import sys
	input = sys.stdin.read
	data = input().split()

	n = int(data[0])
	m = int(data[1])
	seq = [int(data[i + 2]) for i in range(n)]

	index = 2 + n
	results = []

	for _ in range(m):
		i = int(data[index])
		j = int(data[index + 1])
		k = int(data[index + 2])
		part = sorted(seq[i - 1:j])
		results.append(part[k - 1])
		index += 3

	for result in results:
		print(result)

if __name__ == "__main__":
	main()