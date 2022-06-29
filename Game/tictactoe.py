import numpy as np
from check import endcheck, Check_draw
from minmax import minmaxalgo

# Generally the board size will be 3x3
base_ = np.zeros((3, 3))


def Print(base_):
    for i in range(3):
        print("|", end="")
        for j in range(3):
            if base_[i][j] == 1:
                print("X", end="")
            if base_[i][j] == 0:
                print(" ", end="")
            if base_[i][j] == -1:
                print("O", end="")
            print("|", end="")
        print("\n")


def valid(x, y):
    if(base_[int(x)][int(y)] == 0):
        return 1
    else:
        return 0


def MyChoice():
    least = 100
    x = 0
    y = 0
    for i in range(3):
        for j in range(3):
            if base_[i][j] == 0:
                base_[i][j] = -1
                score = minmaxalgo(base_, 0, True)
                base_[i][j] = 0
                if score < least:
                    least = score
                    x, y = i, j
    return x, y


k = 0
# Toss to decide who to start
print("*********Toss*********\n")
toss = input("Enter either heads or tails: ")
value = np.random.randint(0, 2, size=1)
if(toss == "heads"):
    if(value == 1):
        print("You won.\n")
        while endcheck(base_) == 0:
            j = k % 2
            if j == 0:
                x, y = input(
                    "Please enter your move in x,y co-ordinates ").split()
                while not valid(x, y):
                    print("please enter valid co-ordinates, place is already occupied!")
                    x, y = input(
                        "Please enter your move in x,y co-ordinates ").split()
                base_[int(x)][int(y)] = 1
            else:
                x, y = MyChoice()
                base_[x][y] = -1
            if(j == 0):
                print("after your turn: \n")
            else:
                print("after my turn: \n")
            k += 1

            Print(base_)

        z = endcheck(base_)
        if z == 1:
            print("You are the winner")
        if z == -1:
            print("Hooray! I am the winner")
        if z == 2:
            print("It's a draw")
    else:
        print("I won. So I start the game\n")
        x = np.random.randint(0, 3, size=1)
        y = np.random.randint(0, 3, size=1)
        base_[x[0]][y[0]] = -1
        Print(base_)
        while endcheck(base_) == 0:
            j = k % 2
            if j == 0:
                x, y = input(
                    "Please enter your move in x,y co-ordinates ").split()
                while not valid(x, y):
                    print("please enter valid co-ordinates, place is already occupied!")
                    x, y = input(
                        "Please enter your move in x,y co-ordinates ").split()
                base_[int(x)][int(y)] = 1
            else:
                x, y = MyChoice()
                base_[x][y] = -1
            if(j == 0):
                print("after your turn: \n")
            else:
                print("after my turn: \n")
            k += 1
            Print(base_)

        z = endcheck(base_)
        if z == 1:
            print("You are the winner")
        if z == -1:
            print("Hooray! I am the winner")
        if z == 2:
            print("It's a draw")


elif(toss == "tails"):
    if(value == 0):
        print("You won.\n")
        while endcheck(base_) == 0:
            j = k % 2
            if j == 0:
                x, y = input(
                    "Please enter your move in x,y co-ordinates ").split()
                while not valid(x, y):
                    print("please enter valid co-ordinates, place is already occupied!")
                    x, y = input(
                        "Please enter your move in x,y co-ordinates ").split()
                base_[int(x)][int(y)] = 1
            else:
                x, y = MyChoice()
                base_[x][y] = -1
            if(j == 0):
                print("after your turn: \n")
            else:
                print("after my turn: \n")
            k += 1
            Print(base_)

        z = endcheck(base_)
        if z == 1:
            print("You are the winner")
        if z == -1:
            print("Hooray! I am the winner")
        if z == 2:
            print("It's a draw")
    else:
        print("I won. So I start the game\n")
        x = np.random.randint(0, 3, size=1)
        y = np.random.randint(0, 3, size=1)
        base_[x[0]][y[0]] = -1
        Print(base_)
        while endcheck(base_) == 0:
            j = k % 2
            if j == 0:
                x, y = input(
                    "Please enter your move in x,y co-ordinates ").split()
                while not valid(x, y):
                    print("please enter valid co-ordinates, place is already occupied!")
                    x, y = input(
                        "Please enter your move in x,y co-ordinates ").split()
                base_[int(x)][int(y)] = 1
            else:
                x, y = MyChoice()
                base_[x][y] = -1
            if(j == 0):
                print("after your turn: \n")
            else:
                print("after my turn: \n")
            k += 1
            Print(base_)

        z = endcheck(base_)
        if z == 1:
            print("You are the winner")
        if z == -1:
            print("Hooray! I am the winner")
        if z == 2:
            print("It's a draw")
