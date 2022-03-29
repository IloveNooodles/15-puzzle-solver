from library import *
from time import sleep, time


def solveBranchAndBounds(puzzle):
    nodeCount = 0
    start = time()
    # create priority queue
    pq = PriorityQueue()

    # create root
    root = Node(None, puzzle, zeroIdx(puzzle), countCost(puzzle), 0, "IDLE")
    # enqueue root
    pq.push(root)
    # do bfs
    while(not pq.empty()):
        node = pq.pop()
        # print("=========")
        # print(node.puzzle)
        print(node.puzzle)
        print(node.cost)
        if(node.cost < 10):
            break
        if isSolve(node.cost):
            print("==========")
            printSolution(node)
            print("final gan")
            print(f"Time execution: {time() - start}s")
            return
        # generate node
        for dir in direction:
            zeroIndex = 0
            if(dir == "UP"):
                zeroIndex = UP(node.puzzle, node.zeroIdx)
            elif(dir == "RIGHT"):
                zeroIndex = RIGHT(node.puzzle, node.zeroIdx)
            elif(dir == "LEFT"):
                zeroIndex = LEFT(node.puzzle, node.zeroIdx)
            else:
                zeroIndex = DOWN(node.puzzle, node.zeroIdx)
            if isValidMove(zeroIndex):
                child = createNode(
                    node.puzzle, node.zeroIdx, zeroIndex, node.level + 1, node, dir)
                if not np.array_equal(node.puzzle, child.puzzle):
                    nodeCount += 1
                    pq.push(child)


if __name__ == "__main__":
    # fileName = printDir()
    # t = readPuzzle("correct1.txt")
    # a = zeroIdx(t)
    # DOWN(t, a)
    # # t = createPuzzle()
    # print(countCost(t))
    # zerIdx = zeroIdx(puzzle)
    # newZerIdx = DOWN(puzzle, zerIdx)
    # print(zerIdx, newZerIdx)
    # # root = Node(None)
    # print(puzzle)
    # Node = createNode(puzzle, zerIdx, newZerIdx, 0, None, "IDLE")
    # print(Node.puzzle)
    puzzle = readPuzzle("correct2.txt")
    solveBranchAndBounds(puzzle)
