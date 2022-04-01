import solver

print("Welcome to gare's 15 puzzle solver\nwhat do you want to do?")
while True:
    solver.menu()
    choice = input("> ")
    choice = choice.upper()
    puzzle = None
    if choice == "Q":
        print(
            "\nThank you for using gare's 16-puzzle solver")
        exit(0)
    elif choice == "1":
        puzzle = solver.readPuzzleInput()
    elif choice == "2":
        puzzle = solver.createPuzzle()
    elif choice == "3":
        dir = solver.printDir()
        puzzle = solver.readPuzzle(dir)
    else:
        print("Please input correct option")
        continue
    solver.solve(puzzle)
