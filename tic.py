import random

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
        x = random.randrange(0, 8)
        if t[o] == ".":
                t[o] = "o"
        else:
                continue
        if t[x] == ".":
                t[x] = "x"
