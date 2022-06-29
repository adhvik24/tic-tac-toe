import numpy as np


def endcheck(base_):
    if(base_[0][0] == base_[1][1] == base_[2][2]) and base_[0][0] != 0:
        z = base_[0][0]
        return z
    if(base_[0][2] == base_[1][1] == base_[2][0]) and base_[0][2] != 0:
        z = base_[0][2]
        return z
    for i in range(base_.shape[0]):
        if base_[i][1] == base_[i][0] == base_[i][2] and base_[i][0] != 0:
            z = base_[i][0]
            return z
    for i in range(base_.shape[0]):
        if base_[1][i] == base_[0][i] == base_[2][i] and base_[0][i] != 0:

            z = base_[0][i]
            return z

    if Check_draw(base_):
        return 2
    return 0


def Check_draw(base_):
    for i in range(3):
        for j in range(3):
            if(base_[i][j] == 0):
                return 0
    return 1
