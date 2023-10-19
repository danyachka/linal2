from matplotlib import pyplot as plt
import sympy as s
from colorama import Fore, Style

import matrixGenerator as mG

funcList: []
matrixList = [s.Matrix]


def initAllMatrix():
    global funcList
    funcList = [mG.m1, mG.m2, mG.m3, mG.m4, mG.m5, mG.m6, mG.m7, mG.m8, mG.m9]

    for i in range(len(funcList)):
        func = funcList[i]
        print(Fore.BLUE + "Part №" + str(i + 1) + Style.RESET_ALL)
        m = func()
        print(m)
        print("\n")


if __name__ == '__main__':
    initAllMatrix()
    plt.show()
