from library import *

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
    print("Thank you for using gare's 15-puzzle solver\n=================")


def BranchAndBounds(puzzle):
    solutionPath = []
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
        if node.cost == 0:
            print("==========")
            printSolution(node, solutionPath)
            print(solutionPath)
            print(f"Time execution: {time() - start}s")
            print(f"Generated node count: {nodeCount}")
            print(f"Move needed: {len(solutionPath)}")
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
                newPuzzle = createNextPuzzle(
                    node.puzzle, node.zeroIdx, zeroIndex)
                # child = createNode(
                #     node.puzzle, node.zeroIdx, zeroIndex, node.level + 1, node, dir)
                newPuzzleBytes = newPuzzle.tobytes()
                if newPuzzleBytes not in visited:
                    child = Node(node, newPuzzle, zeroIndex,
                                 countCost(newPuzzle), node.level + 1, dir)
                    visited[newPuzzleBytes] = True
                    nodeCount += 1
                    pq.put(child)


if __name__ == "__main__":
    puzzle = readPuzzle("correct7.txt")
    solve(puzzle)
