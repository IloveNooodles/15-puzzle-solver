import numpy as np
import os
from random import shuffle
from heapq import heappush, heappop

direction = ["UP", "RIGHT", "DOWN", "LEFT"]
target = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]
target = np.reshape(target, (4, 4))


class PriorityQueue:
    def __init__(self):
        self.heap = []

    def push(self, k):
        heappush(self.heap, k)

    def pop(self):
        return heappop(self.heap)

    def empty(self):
        if not self.heap:
            return True
        else:
            return False


class Node:
    def __init__(self, parent, puzzle, zeroIdx, cost, level, state):
        self.parent = parent
        self.puzzle = puzzle
        self.zeroIdx = zeroIdx
        self.level = level
        self.cost = cost
        self.state = state

    def __lt__(self, next):
        return self.cost < next.cost


def createNode(puzzle, zeroIdx, newZeroIdx, level, parent, state):
    newPuzzle = np.copy(puzzle)
    row1, col1 = zeroIdx
    row2, col2 = newZeroIdx
    newPuzzle[row1, col1], newPuzzle[row2,
                                     col2] = newPuzzle[row2, col2], newPuzzle[row1, col1]

    node = Node(parent, newPuzzle, newZeroIdx,
                countCost(newPuzzle) + level, level, state)

    return node


def printSolution(root):
    if root == None:
        return
    printSolution(root.parent)
    print(root.puzzle)
    print(f"============\nMOVE: {root.state}\n============",)


def kurangNumber(puzzle, rowIdx, colIdx):
    kurang = 0
    size = len(puzzle)
    target = puzzle[rowIdx, colIdx]
    if target == 0:
        target = 16
    while rowIdx < size:
        while colIdx < size:
            if target > puzzle[rowIdx, colIdx] and puzzle[rowIdx, colIdx] != 0:
                kurang += 1
            colIdx += 1
        colIdx = 0
        rowIdx += 1
    return kurang

# kurang function


def kurangFunction(puzzle):
    sum = 0
    for row in range(4):
        for col in range(4):
            if puzzle[row, col] == 0 and ((row % 2 == 0 and col % 2 == 1) or (row % 2 == 1 and col % 2 == 0)):
                sum += 1
            sum += kurangNumber(puzzle, row, col)
    return sum


def cetakKurang(puzzle):
    for row in range(4):
        for col in range(4):
            num = kurangNumber(puzzle, row, col)
            if puzzle[row, col] == 0:
                print(f"16\t: {num}")
            else:
                print(f"{puzzle[row, col]}\t: {num}")
# check if solvable or not using kurang formula


def isSolvable(kurangNumber):
    return kurangNumber % 2 == 0


def solve(puzzle):
    print("Start state of puzzle\n=================")
    print(puzzle)
    print("=================")
    print("Value of kurang i\n=================")
    cetakKurang(puzzle)
    kurang = kurangFunction(puzzle)
    print("=================")
    print("Value of kurang function: ", kurang)
    if isSolvable(kurang):
        # solve
        print("The path solutions are\n")
    else:
        print("The puzzle cannot be solved from this first state\n")
    print("Thank you for using 15-puzzle solver\n=================")


def createPuzzle():
    puzzle = np.arange(0, 16)
    shuffle(puzzle)
    puzzle = np.reshape(puzzle, (4, 4))
    return puzzle


def printDir():
    listdir = os.listdir(f"{os.getcwd()}\\test")
    print("Select puzzle file you want to solve")
    for i in range(len(listdir)):
        print(f"{i+1}. {listdir[i]}")
    choice = int(input("Select file number: "))
    try:
        return listdir[choice - 1]
    except:
        print("Please select correct number")
        printDir()


def readPuzzle(fileName):
    puzzle = []
    path = os.getcwd()
    path += f"\\test\\{fileName}"
    try:
        with open(path) as f:
            lines = f.readlines()
            for line in lines:
                puzzle.append(list(map(int, line.split())))
        return np.reshape(puzzle, (4, 4))
    except:
        print("Wrong file format. Program exiting...")
        exit(0)


def zeroIdx(puzzle):
    idx = 0
    for rows in range(4):
        for cols in range(4):
            if puzzle[rows, cols] == 0:
                return (rows, cols)

    return -1


def isValidMove(zeroIdx):
    row, col = zeroIdx
    return (0 <= row < 4) and (0 <= col < 4)

# Move 4 direction


def UP(puzzle, zeroIdx):
    row, col = zeroIdx
    return (row - 1, col)


def RIGHT(puzzle, zeroIdx):
    row, col = zeroIdx
    return (row, col + 1)


def DOWN(puzzle, zeroIdx):
    row, col = zeroIdx
    return (row + 1, col)


def LEFT(puzzle, zeroIdx):
    row, col = zeroIdx
    return (row, col - 1)


def countCost(puzzle):
    cost = 0
    for row in range(4):
        for col in range(4):
            if puzzle[row, col] != target[row, col] and puzzle[row, col] != 0:
                cost += 1
    return cost


def isSolve(cost):
    return cost == 0
