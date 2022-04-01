import numpy as np
import os
from random import shuffle
from queue import PriorityQueue
from time import sleep, time

direction = ["UP", "RIGHT", "DOWN", "LEFT"]
target = np.reshape([[1, 2, 3, 4], [5, 6, 7, 8], [
                    9, 10, 11, 12], [13, 14, 15, 0]], (4, 4))

solutionPath = 0


class Node:  # Node class
    def __init__(self, parent, puzzle, zeroIdx, cost, level, state):
        self.parent = parent
        self.puzzle = puzzle
        self.zeroIdx = zeroIdx
        self.level = level
        self.cost = cost
        self.state = state

    def __lt__(self, next):
        return self.cost + self.level <= next.cost + next.level


# create next puzzle based on move
def createNextPuzzle(puzzle, zeroIdx, newZeroIdx, costBefore):
    newPuzzle = np.copy(puzzle)
    row1, col1 = zeroIdx
    row2, col2 = newZeroIdx
    before, after = False, False
    if newPuzzle[row2, col2] == target[row2, col2]:
        before = True
    newPuzzle[row1, col1], newPuzzle[row2,
                                     col2] = newPuzzle[row2, col2], newPuzzle[row1, col1]
    if newPuzzle[row1, col1] == target[row1, col1]:
        after = True

    if before == False and after == True:
        costBefore -= 1

    if before == True and after == False:
        costBefore += 1
    return newPuzzle, costBefore


def printSolution(root, solution):  # print all possible solution
    if root == None:
        return
    printSolution(root.parent, solution)
    print(
        f"================================\n{root.puzzle}\n MOVE: {root.state}\n================================\n")
    solution.append(root.state)


def zeroIdx(puzzle):  # find zero index
    idx = 0
    for rows in range(4):
        for cols in range(4):
            if puzzle[rows, cols] == 0:
                return (rows, cols)

    return -1


def isValidMove(zeroIdx):  # to check if move is valid
    row, col = zeroIdx
    return (0 <= row < 4) and (0 <= col < 4)


def UP(puzzle, zeroIdx):  # move up
    row, col = zeroIdx
    return (row - 1, col)


def RIGHT(puzzle, zeroIdx):  # move right
    row, col = zeroIdx
    return (row, col + 1)


def DOWN(puzzle, zeroIdx):  # move down
    row, col = zeroIdx
    return (row + 1, col)


def LEFT(puzzle, zeroIdx):  # move left
    row, col = zeroIdx
    return (row, col - 1)


def countCost(puzzle):  # count cost with matching tile
    cost = 0
    for row in range(4):
        for col in range(4):
            if puzzle[row, col] != target[row, col] and puzzle[row, col] != 0:
                cost += 1
    return cost


def kurangNumber(puzzle, rowIdx, colIdx):  # calculate less number in the puzle
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


def kurangFunction(puzzle):  # calculate all less number in the puzzle
    sum = 0
    for row in range(4):
        for col in range(4):
            if puzzle[row, col] == 0 and ((row % 2 == 0 and col % 2 == 1) or (row % 2 == 1 and col % 2 == 0)):
                sum += 1
            sum += kurangNumber(puzzle, row, col)
    return sum


def cetakKurang(puzzle):  # print all kurang number in the puzzle
    for row in range(4):
        for col in range(4):
            num = kurangNumber(puzzle, row, col)
            if puzzle[row, col] == 0:
                print(f"16\t: {num}")
            else:
                print(f"{puzzle[row, col]}\t: {num}")


def isSolvable(kurangNumber):  # check if solvable or not using kurang formula
    return kurangNumber % 2 == 0


def createPuzzle():  # create random puzzle
    puzzle = np.arange(0, 16)
    shuffle(puzzle)
    puzzle = np.reshape(puzzle, (4, 4))
    return puzzle


def printDir():  # print list directory on test folder
    os.listdir = os.listdir(f"{os.getcwd()}//test")
    print("Select puzzle file you want to solve")
    for i in range(len(os.listdir)):
        print(f"{i+1}. {os.listdir[i]}")
    choice = int(input("> "))
    try:
        return os.listdir[choice - 1]
    except:
        print("Please select correct number")
        printDir()


def readPuzzle(fileName):  # read puzzle from txt file
    puzzle = []
    path = os.getcwd()
    path += f"//test//{fileName}"
    try:
        with open(path) as f:
            lines = f.readlines()
            for line in lines:
                puzzle.append(list(map(int, line.split())))
        return np.reshape(puzzle, (4, 4))
    except:
        print("Wrong file format. Program exiting...")
        exit(0)


def readPuzzleInput():
    print("Input unique number between 1 - 15 (put 0 for empty space)")
    print("The number you choose is 4 per line ex: 1 2 3 4 (seperated by whitespace)")
    puz = []
    correct = 0
    number = set()
    while correct < 4:
        foundDuplicate = False
        line = input("> ")
        toAdd = list(map(int, line.split()))

        # check len
        if len(toAdd) != 4:
            print("Please input correct format")
            continue

        # check if there are duplicate number
        for num in toAdd:
            if num in number:
                print(f"{num} is duplicate number")
                foundDuplicate = True
                break

        if foundDuplicate:
            continue
        # insert to set
        for num in toAdd:
            number.add(num)

        if len(toAdd) == 4:
            puz.append(toAdd)
            correct += 1

    print("\n")
    return np.reshape(puz, (4, 4))


def menu():
    print("What do you want to do?")
    print("[1] Read puzzle from input user")
    print("[2] Generate random puzzle")
    print("[3] Read Puzzle from file")
    print("[Q] Exit The Program")
