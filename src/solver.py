import numpy as np
import os
from random import shuffle


def branchAndBounds(puzzle):
    print("test")


def kurangNumber(puzzle, rowIdx, colIdx):
    kurang = 0
    size = len(puzzle)
    target = puzzle[rowIdx][colIdx]
    if target == 0:
        target = 16
    while rowIdx < size:
        while colIdx < size:
            if target > puzzle[rowIdx][colIdx] and puzzle[rowIdx][colIdx] != 0:
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
            if puzzle[row][col] == 0 and ((row % 2 == 0 and col % 2 == 1) or (row % 2 == 1 and col % 2 == 0)):
                sum += 1
            num = kurangNumber(puzzle, row, col)
            if puzzle[row][col] == 0:
                print(f"16\t: {num}")
            else:
                print(f"{puzzle[row][col]}\t: {num}")
            sum += kurangNumber(puzzle, row, col)
    return sum

# check if solvable or not using kurang formula


def isSolvable(kurangNumber):
    return kurangNumber % 2 == 0

# make a random array


def solve(puzzle):
    print("Start state of puzzle\n=================")
    print(puzzle)
    print("=================")
    print("Value of kurang i\n=================")
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
        print("File is empty, program exiting...")
        exit(0)


fileName = printDir()
t = readPuzzle(fileName)
print(t)
# solve(t)
