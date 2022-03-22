t = [".",".",".",".",".",".",".",".","."]

def dis():
	print("  0    1    2")
	print(t[:3])
	print("  3    4    5")
	print(t[3:6])
	print("  6    7    8")
	print(t[6:9])

while True:
	dis()
	o = int(input())
	if t[o] == ".":
		t[o] = "o"