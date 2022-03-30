from library import *
from time import sleep, time

# hashmap of visited state
visited = {}


def solve(puzzle):  # main function
    print("Start state of puzzle\n=================")
    print(puzzle)
    print("=================")
    print("Value of kurang i\n=================")
    cetakKurang(puzzle)
    kurang = kurangFunction(puzzle)
    print("=================")
    print("Value of kurang function: ", kurang)
    if isSolvable(kurang):
        print("The path solutions are\n")
        BranchAndBounds(puzzle)
    else:
        print("The puzzle cannot be solved from this first state\n")
    print("Thank you for using 15-puzzle solver\n=================")


def BranchAndBounds(puzzle):
    nodeCount = 0
    start = time()
    # create priority queue
    pq = PriorityQueue()

    # create root
    root = Node(None, puzzle, zeroIdx(puzzle), countCost(puzzle), 0, "IDLE")
    # enqueue root
    pq.put(root)
    # do bfs
    visited[root.puzzle.tobytes()] = True
    while(not pq.empty()):
        node = pq.get()
        # print("=========")
        # print(node.puzzle)
        # print(node.puzzle)
        # print(node.cost)
        if node.cost == 0:
            print("==========")
            printSolution(node)
            print(f"Time execution: {time() - start}s")
            print(f"Generated node count: {nodeCount}")
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
                nodeCount += 1
                if child.puzzle.tobytes() not in visited:
                    visited[child.puzzle.tobytes()] = True
                    pq.put(child)


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
    solve(puzzle)
