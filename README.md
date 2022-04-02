# 15-puzzle-solver

This repository is made to fulfill Tugas Kecil 1 Strategi Algoritma 2022. 15 Puzzle Solver made using python and using the principles of branch and bounds algorithm.

## Screenshots

![image](https://user-images.githubusercontent.com/63847012/161382493-215cd9f9-a91d-4186-9373-ab3966eca344.png)
![image](https://user-images.githubusercontent.com/63847012/161382521-0192b86c-f1d0-4e07-9f05-8b133e813936.png)

## Technologies used

1. [Python (3.8+)](https://www.python.org/)
2. [Numpy](https://numpy.org/)

## Feature

This programs will output least amount move possilbe to solve the puzzle using branch and bounds algorithm. **(BEWARE that some puzzle will take time to compute so please wait :))**

## Setup

1. Install requirement from the `technologies section`
2. Clone the repository using `git clone https://github.com/IloveNooodles/15-puzzle-solver.git`
3. Open the folder and move to src using `cd src`
4. **Make sure you are in the src directory otherwise it won't work**
5. Run the file using `python main.py`

## Input

1. Input is unique number from 1 to 15
2. **Use 0 for empty space**
3. template for text file

```md
1 2 3 4
5 6 7 8
9 0 10 11
12 13 14 15
```

## Usage

1. You can choose either input from txt file, input line by line or generate random puzzle
2. Make sure your input is correct
3. Ta-da! program will output move and steps by steps

## Room for improvement

1. Make GUI for program to better visualization
2. Better approach in the algorithm for faster runtime

## Folder structure

```md
├── README.md
├── doc
│   └── Tucil3_13520029.pdf       
├── src
│   ├── library.py
│   ├── main.py
│   └── solver.py
└── test
    ├── correct1.txt
    ├── correct2.txt
    ├── correct3.txt
    ├── correct4.txt
    ├── correct5.txt
    ├── false1.txt
    └── false2.txt
```
### Made with ❤ by IloveNooodles

