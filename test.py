t = [".",".",".",".",".",".",".",".","."]

def dis():
	print(t[:3])
	print(t[3:6])
	print(t[6:9])

while True:
	dis()
	o = input()
	t[o] = "o"