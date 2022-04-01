import library
import solver
import numpy as np
from os import getcwd
from time import sleep
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

# bakal ada 3 frame
# header, puzzle, sama button

buttonRef = {}


class GUI:
    def __init__(self, window):
        self.pathfile = None
        self.puzzle = None
        self.listState = None
        self.run = False
        self.window = window
        self.quit = False
        self.zeroIdx = (0, 0)

    def startGUI(self):
        self.window.geometry('640x480')
        self.window.title("Gare's 15 puzzle solver")
        self.window.configure(bg="#55423d")
        self.window.resizable(False, False)
        # heading
        label = Label(
            self.window, text="Welcome to Gare's 15 puzzle solver!", font=("Consolas", 20), background="#55423d", fg="#fffffe", name="heading")
        label.pack(side=TOP, pady=10)
        puzzframe = Frame(self.window,  bg="#ffc0ad", relief=GROOVE,
                          highlightbackground="#140d0b", highlightthickness=1, name="puzzframe")
        # puzzframe
        for i in range(4):
            for j in range(4):
                text = ""
                # cell = Frame(puzzframe, highlightbackground="#140d0b",
                #              highlightthickness=1, bg="#fff3ec", relief=GROOVE, name=f"cell{(i*4 + j) + 1}")
                # label = Label(cell, text=text,
                #               font=("Consolas", 16), bg="#fff3ec", width=5, height=3, name=f"label{(i*4 + j) + 1}")
                # label.pack()
                # cell.grid(row=i, column=j)
                # print(cell.winfo_children())

                label = Label(puzzframe, text=text,
                              font=("Consolas", 16), bg="#fff3ec", width=5, height=3, name=f"label{(i*4 + j) + 1}", highlightbackground="blue",
                              highlightthickness=1)
                label.grid(row=i, column=j)
                buttonRef[(i, j)] = label
        puzzframe.pack(side=TOP)

        # quit button and start
        frameButton = Frame(self.window, bg="#55423d",
                            relief=FLAT, name="button frame")
        solveButton = Button(frameButton, text="Solve", width=8, height=2, bg="#ffc0ad",
                             relief=FLAT, fg="#271c19", font=("Consolas"), name="solve button", command=self.solve)
        solveButton.grid(row=0, column=1, padx=10, pady=5)
        quitButton = Button(frameButton, text="Quit", width=8,
                            height=2, command=self.quitFunction, bg="#ffc0ad", relief=FLAT, fg="#271c19", font=("Consolas"), name="quit button")
        quitButton.grid(row=0, column=2, padx=10, pady=5)
        browse = Button(frameButton, name="browse folder", text="Start",
                        width=8, height=2, bg="#ffc0ad", relief=FLAT, fg="#271c19", font=("Consolas"), command=self.browseFolder)
        browse.grid(row=0, column=0, padx=10, pady=5)
        frameButton.pack(side=TOP, pady=10)

    def browseFolder(self):
        currdir = getcwd()
        self.window.sourceFile = filedialog.askopenfile(
            parent=self.window, initialdir=currdir, title='Please select a directory')
        self.pathfile = self.window.sourceFile.name
        self.zeroIdx = self.openFile()

    def openFile(self):
        puz = []
        zeroIndex = 0
        with open(self.pathfile) as f:
            lines = f.readlines()
            for line in lines:
                puz.append(list(map(int, line.split())))
        self.puzzle = np.reshape(puz, (4, 4))
        for i in range(4):
            for j in range(4):
                buttonRef[(i, j)].configure(text=self.puzzle[i, j])
                if self.puzzle[i, j] == 0:
                    zeroIndex = (i, j)
        return zeroIndex

    def solve(self):
        if not self.run:
            print(self.listState, self.pathfile,
                  self.puzzle, self.quit, self.run)
            self.listState = solver.BranchAndBounds(self.puzzle, True)
            self.run = True
            print(self.listState)
            self.runFunction()

    def runFunction(self):
        if not self.run:
            print("Please select file first")
            return

        for i in range(len(self.listState)):
            self.changeState(self.listState[i])
            sleep(2)
            # row, col = self.zeroIdx
            # if self.listState[i] == "UP":
            #     temp = self.puzzle[row, col]
            #     self.puzzle[row, col] = self.puzzle[row - 1, col]
            #     self.puzzle[row - 1, col] = temp
            #     self.zeroIdx = (row - 1, col)
            # elif self.listState[i] == "DOWN":
            #     temp = self.puzzle[row, col]
            #     self.puzzle[row, col] = self.puzzle[row + 1, col]
            #     self.puzzle[row + 1, col] = temp
            #     self.zeroIdx = (row + 1, col)
            # elif self.listState[i] == "RIGHT":
            #     temp = self.puzzle[row, col]
            #     self.puzzle[row, col] = self.puzzle[row, col + 1]
            #     self.puzzle[row, col + 1] = temp
            #     self.zeroIdx = (row, col + 1)
            # elif self.listState[i] == "LEFT":
            #     temp = self.puzzle[row, col]
            #     self.puzzle[row, col] = self.puzzle[row, col - 1]
            #     self.puzzle[row, col - 1] = temp
            #     self.zeroIdx = (row, col - 1)
            # else:
            #     continue
            # # awalnya col row zero skrg newrow newcol jd zero
            # newRow, newCol = self.zeroIdx
            # test = self.window.winfo_children()[1]
            # test = test.winfo_children()
            # print(test[0].config()["text"][4])
            # test[row*4 + col].configure(text=self.puzzle[row, col])
            # test[newRow*4 + newCol].configure(text=self.puzzle[newRow, newCol])
            # sleep(2)
            # # buttonRef[(row, col)].configure(text=self.puzzle[row, col])
            # # buttonRef[(newRow, newCol)].configure(
            # #     text=self.puzzle[newRow, newCol])
        self.run = False

    def changeState(self, state):
        row, col = self.zeroIdx
        if state == "UP":
            temp = self.puzzle[row, col]
            self.puzzle[row, col] = self.puzzle[row - 1, col]
            self.puzzle[row - 1, col] = temp
            self.zeroIdx = (row - 1, col)
        elif state == "DOWN":
            temp = self.puzzle[row, col]
            self.puzzle[row, col] = self.puzzle[row + 1, col]
            self.puzzle[row + 1, col] = temp
            self.zeroIdx = (row + 1, col)
        elif state == "RIGHT":
            temp = self.puzzle[row, col]
            self.puzzle[row, col] = self.puzzle[row, col + 1]
            self.puzzle[row, col + 1] = temp
            self.zeroIdx = (row, col + 1)
        elif state == "LEFT":
            temp = self.puzzle[row, col]
            self.puzzle[row, col] = self.puzzle[row, col - 1]
            self.puzzle[row, col - 1] = temp
            self.zeroIdx = (row, col - 1)
        elif state == "IDLE":
            return

        newRow, newCol = self.zeroIdx
        test = self.window.winfo_children()[1]
        test = test.winfo_children()
        print(test[0].config()["text"][4])
        test[row*4 + col].configure(text=self.puzzle[row, col])
        test[newRow*4 + newCol].configure(text=self.puzzle[newRow, newCol])

    def quitFunction(self):
        messagebox.showinfo(
            "App closing", "Thankyou for using Gare's 15 puzzle solver")
        self.quit = True
        exit(0)


def mainGUI():
    window = Tk()
    gui = GUI(window)
    gui.startGUI()
    gui.window.mainloop()


if __name__ == "__main__":
    mainGUI()
