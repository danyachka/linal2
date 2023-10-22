from matplotlib import pyplot as plt
from typing import Final
from enum import Enum
import math
import numpy as np
import sympy as s
import matrix_generator

MAX_X_AND_Y: Final[float] = 5
BIG_NUMBER: Final[float] = 120

square: [s.Matrix] = [s.Matrix([[1], [1]]), s.Matrix([[0], [2]]), s.Matrix([[-1], [1]]), s.Matrix([[-0.5], [-1]]),
                      s.Matrix([[0.5], [-1]]), s.Matrix([[1], [1]])]

legendList = ["До преобразований", "Преобразованный график №", "График "]
styleList = ["-D", "-.o", "-.D", "-."]


class Color(Enum):
    red = "Red"
    green = "Green"
    blue = "Blue"
    pink = "Pink"
    black = "Black"


class Plot:
    points: [s.Matrix]
    color: Color
    m: s.Matrix
    style: str
    linesColor: Color
    plotName: str

    def __init__(self, points: [s.Matrix], color: Color, m: s.Matrix = None,
                 style=None, linesColor: Color = Color.black, plotName: str = None):
        self.points = points
        self.color = color
        self.m = m
        self.style = style
        self.linesColor = linesColor
        self.plotName = plotName


def drawColoredPlots(plots: [Plot], number: int, lineA=False, lineB=False):
    fig = plt.figure(figsize=(7, 7))
    ax = fig.add_subplot()

    if lineA:
        x = MAX_X_AND_Y
        y = matrix_generator.a * x
        ax.plot([-x, x], [-y, y], "--", color=Color.black.value, label="y=ax")
    if lineB:
        x = MAX_X_AND_Y
        y = matrix_generator.b * x
        ax.plot([-x, x], [-y, y], "--", color=Color.black.value, label="y=bx")

    for i in range(len(plots)):
        plot = plots[i]
        l = len(plot.points)
        pX = [plot.points[i][0, 0] for i in range(l)]
        pY = [plot.points[i][1, 0] for i in range(l)]

        if plot.plotName is not None:
            legend = legendList[2] + plot.plotName
        elif i == 0:
            legend = legendList[0]
        else:
            legend = legendList[1] + str(i)

        style = "--"
        if plot.style is not None:
            style = plot.style
        elif i < len(styleList):
            style = styleList[i]

        if plot.m is not None:
            array = getEigenvectors(plot.m)
            for v in array:
                x = BIG_NUMBER * v[0, 0]
                y = BIG_NUMBER * v[1, 0]
                ax.plot([-x, x], [-y, y], ":", color=plot.linesColor.value, label="Ось собственного вектора")

        ax.plot(pX, pY, style, color=plot.color.value, label=legend)

    ax.set_xlim([-MAX_X_AND_Y, MAX_X_AND_Y])
    ax.set_ylim([-MAX_X_AND_Y, MAX_X_AND_Y])

    ax.legend()
    ax.grid()

    ax.set_title("Пункт №" + str(number))
    plt.show()


def rotate(m: s.Matrix, alfa):
    t: s.Matrix = s.zeros(2)
    sin = s.sin(alfa)
    cos = s.cos(alfa)

    t[0, 0] = cos
    t[0, 1] = sin
    t[1, 0] = -sin
    t[1, 1] = cos

    m = t.inv() * m * t
    return m


def createCircleAndOtherPlot(m: s.Matrix, number):
    count = 100
    angles = np.linspace(0, 2 * math.pi, count)
    x1 = 1 * np.cos(angles)
    y1 = 1 * np.sin(angles)

    real = []
    changed = []
    for i in range(count):
        vi: s.Matrix = s.Matrix([[0], [0]])
        vi[0, 0] = x1[i]
        vi[1, 0] = y1[i]
        vj = m * vi

        real.append(vi)
        changed.append(vj)

    plots = [Plot(real, Color.red, style="-"), Plot(changed, Color.green, style="--")]
    drawColoredPlots(plots, number)


def getEigenvectors(m: s.Matrix) -> [s.Matrix]:
    array = m.eigenvects()
    sym_eigenvectors: [s.Matrix] = []
    for tup in array:
        for v in tup[2]:
            numbers = list(v)
            if not hasComplex(numbers):
                sym_eigenvectors.append(v)
    return sym_eigenvectors


def hasComplex(array: []) -> bool:
    for n in array:
        if "I" in str(n):
            return True
    return False


def convertPoints(array, m: s.Matrix) -> [s.Matrix]:
    result = []
    for v in array:
        result.append(m * v)
    return result


def printEigenValues(m: s.Matrix):
    vals = m.eigenvects()
    pos = 1
    print("Спектральный анализ:")
    for value in vals:
        print(str(pos) + ") Собственное число - " + str(round(value[0], 2)) + ". Собственные векторы:")
        for v in value[2]:
            print("\t" + str(list(v)))
        pos += 1


def printCoreAndRange(m: s.Matrix):
    nullspace = m.nullspace()
    span = m.columnspace()

    print("\nЯдро матрицы:")
    if len(nullspace) == 0:
        print("\t{0}")
    else:
        for v in nullspace:
            print("\t" + str(list(v)))

    print("\nОбраз матрицы:")
    if len(span) == 0:
        print("\t{0}")
    else:
        for v in span:
            print("\t" + str(list(v)))
