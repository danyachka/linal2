from matplotlib import pyplot as plt
from colorama import Fore, Style
from typing import Final
import sympy as s

import Utils
import matrixGenerator as mG

funcList: []
matrixList = [s.Matrix]

needCore: Final[set] = {1, 2, 13, 14}
needEigenValues: Final[set] = {1, 2, 3, 4, 8, 11, 12, 13, 14, 15, 16}
needDet: Final[set] = {1, 2, 3, 4, 5, 9, 10}


def initAllMatrix():
    global funcList
    funcList = [mG.m1, mG.m2, mG.m3, mG.m4, mG.m5, mG.m6, mG.m7, mG.m8,
                mG.m9, mG.m10, mG.m11, mG.m12, mG.m13, mG.m14, mG.m15, mG.m16]

    for i in range(len(funcList)):
        func = funcList[i]
        pos = i + 1
        print(Fore.BLUE + "Part №" + str(pos) + Style.RESET_ALL)
        m = func()
        if m is not None:
            print("Матрица переобразований - " + str(m))

        if pos in needDet:
            print("\nОпределитель - " + str(round(m.det(), 2)))
        if pos in needCore:
            Utils.printCoreAndRange(m)
        if pos in needEigenValues and m is not None:
            print()
            Utils.printEigenValues(m)
        print("\n")


if __name__ == '__main__':
    s.init_printing(use_unicode=True)
    initAllMatrix()
