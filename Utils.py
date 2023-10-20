from matplotlib import pyplot as plt
from typing import Final
import math
import numpy as np
import sympy as s
import matrixGenerator

MAX_X_AND_Y: Final[float] = 5
BIG_NUMBER: Final[float] = 120

square: [s.Matrix] = [s.Matrix([[1], [1]]), s.Matrix([[0], [2]]), s.Matrix([[-1], [1]]), s.Matrix([[-0.5], [-1]]),
                      s.Matrix([[0.5], [-1]]), s.Matrix([[1], [1]])]


def drawColoredPoints(red: [s.Matrix], green: [s.Matrix], lineA=False, lineB=False,
                      matrix: s.Matrix = None, blue: [s.Matrix] = None):
    fig = plt.figure(figsize=(7, 7))
    greenX = [green[i][0, 0] for i in range(len(green))]
    greenY = [green[i][1, 0] for i in range(len(green))]
    redX = [red[i][0, 0] for i in range(len(red))]
    redY = [red[i][1, 0] for i in range(len(red))]

    ax = fig.add_subplot()
    ax.plot(redX, redY, "-o", color="red", label="До преобразований")
    ax.plot(greenX, greenY, ":o", color="green", label="Преобразованный график")
    ax.grid()

    if lineA:
        x = MAX_X_AND_Y
        y = matrixGenerator.a * x
        ax.plot([-x, x], [-y, y], "--", color="Blue")
    if lineB:
        x = MAX_X_AND_Y
        y = matrixGenerator.b * x
        ax.plot([-x, x], [-y, y], "--", color="Blue")
    if matrix is not None:
        array = getEigenvectors(matrix)
        for v in array:
            x = BIG_NUMBER * v[0, 0]
            y = BIG_NUMBER * v[1, 0]
            ax.plot([-x, x], [-y, y], "--", color="Blue", label="Ось собственного вектора")
    if blue is not None:
        blueX = [blue[i][0, 0] for i in range(len(blue))]
        blueY = [blue[i][1, 0] for i in range(len(blue))]
        ax.plot(blueX, blueY, "-.", color="blue", label="Второй вариант преобразований")
    ax.legend()

    ax.set_xlim([-MAX_X_AND_Y, MAX_X_AND_Y])
    ax.set_ylim([-MAX_X_AND_Y, MAX_X_AND_Y])
    plt.show()


def drawPlots(x1, y1, x2, y2):
    fig = plt.figure(figsize=(7, 7))
    ax = fig.add_subplot()

    ax.plot(x1, y1, "-", color="r", label="До преобразований")
    ax.plot(x2, y2, "-.", color="g", label="Преобразованный график")

    ax.grid()
    ax.legend()

    ax.set_xlim([-MAX_X_AND_Y, MAX_X_AND_Y])
    ax.set_ylim([-MAX_X_AND_Y, MAX_X_AND_Y])
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


def createCircleAndOtherPlot(m: s.Matrix):
    count = 100
    angles = np.linspace(0, 2 * math.pi, count)
    x1 = 1 * np.cos(angles)
    y1 = 1 * np.sin(angles)
    x2 = np.empty((count))
    y2 = np.empty((count))

    v: s.Matrix = s.Matrix([[0], [0]])
    for i in range(count):
        v[0, 0] = x1[i]
        v[1, 0] = y1[i]
        v = m * v
        x2[i] = v[0, 0]
        y2[i] = v[1, 0]

    drawPlots(x1, y1, x2, y2)


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
    if len(nullspace) == 0:
        nullspace.append("{0}")
    span = m.columnspace()
    if len(span) == 0:
        span.append("{0}")

    print("\nЯдро матрицы:")
    for v in nullspace:
        print("\t" + str(list(v)))

    print("\nОбраз матрицы:")
    for v in span:
        print("\t" + str(list(v)))
