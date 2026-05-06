# Assignment 4
# Name: Krushna Keshav Garole
# Roll No: C32257


# =========================================
# N-Queens Problem
# =========================================

def is_safe(board, row, col, n):

    # Check column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check left diagonal
    i, j = row - 1, col - 1

    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False

        i -= 1
        j -= 1

    # Check right diagonal
    i, j = row - 1, col + 1

    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False

        i -= 1
        j += 1

    return True


def solve_nqueens(board, row, n):

    # If all queens are placed
    if row == n:
        print_board(board, n)
        return True

    # Try placing queen in every column
    for col in range(n):

        if is_safe(board, row, col, n):

            # Place queen
            board[row][col] = 1

            # Recur for next row
            if solve_nqueens(board, row + 1, n):
                return True

            # Backtracking
            board[row][col] = 0

    return False


def print_board(board, n):

    print("Solution:")

    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
        print()


# Run
n = 4

board = [[0] * n for _ in range(n)]

solve_nqueens(board, 0, n)


# =========================================
# Graph Coloring Problem
# =========================================

def is_safe(v, graph, color, c):

    for i in range(len(graph)):

        # Check adjacent vertices
        if graph[v][i] == 1 and color[i] == c:
            return False

    return True


def solve_graph_coloring(graph, m, color, v):

    # If all vertices are colored
    if v == len(graph):
        print("Solution:", color)
        return True

    # Try different colors
    for c in range(1, m + 1):

        if is_safe(v, graph, color, c):

            color[v] = c

            # Recur for next vertex
            if solve_graph_coloring(graph, m, color, v + 1):
                return True

            # Backtracking
            color[v] = 0

    return False


# Graph (Adjacency Matrix)
graph = [
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 0]
]

m = 3   # Number of colors

color = [0] * len(graph)

solve_graph_coloring(graph, m, color, 0)