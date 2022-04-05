map_ = [[1, 1, 1, 1, 1, 1,],
        [1, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 0, 1],
        [1, 0, 0, 0, 0, 1],
        [1, 0, 0, 1, 1, 1],
        [1, 1, 1, 1, 1, 1]]
player = [2, 2]

def disp(map_):
        y = 0
        for a in map_:
                x = 0
                y += 1
                for b in a:
                        x += 1
                        if x == player[0] and y == player[1]:
                                print("o", end="")
                        elif b == 1:
                                print("#", end="")
                        elif b == 0:
                                print(" ", end="")
                print("")

def path_clear(tx, ty):
        y = 0
        for a in map_:
                x = 0
                y += 1
                for b in a:
                        x += 1
                        if x == tx and y == ty:
                                if b == 0:
                                        return True
                                else:
                                        return False
                                        

def move():
        direction = input("move: ")
        if direction == "up":
                if path_clear(player[0], player[1] - 1):
                        player[1] -= 1
                else:
                        print("can't move %s" % direction)
        elif direction == "down":
                if path_clear(player[0], player[1] + 1):
                        player[1] += 1
                else:
                        print("can't move %s" % direction)
        elif direction == "left":
                if path_clear(player[0] - 1, player[1]):
                        player[0] -= 1
                else:
                        print("can't move %s" % direction)
        elif direction == "right":
                if path_clear(player[0] + 1, player[1]):
                        player[0] += 1
                else:
                        print("can't move %s" % direction)
        else:
                print("could not parse direction")
                


while True:
        disp(map_)
        move()
        
