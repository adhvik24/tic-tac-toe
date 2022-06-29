import numpy as np
from check import endcheck, Check_draw


def minmaxalgo(base_, depth, Max):
    z = endcheck(base_)
    if z == 1:
        return 1
    if z == -1:
        return -1
    if Check_draw(base_):
        return 0

    if Max:
        maxi = -100
        for i in range(3):
            for j in range(3):
                if base_[i][j] == 0:
                    base_[i][j] = 1
                    score = minmaxalgo(base_, depth+1, False)
                    base_[i][j] = 0
                    if score > maxi:
                        maxi = score
        return maxi
    if not Max:
        least = 100
        for i in range(3):
            for j in range(3):
                if base_[i][j] == 0:
                    base_[i][j] = -1
                    score = minmaxalgo(base_, depth+1, True)
                    base_[i][j] = 0
                    if score < least:
                        least = score
        return least
