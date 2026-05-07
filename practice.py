graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['A','F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E'],
}

def bfs(graph, start):
    
    visited = set()
    queue = []

    visited.add(start)
    queue.append(start)

    while queue:
        node = queue.pop(0)
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# bfs(graph,'A')
#####################################################################################################
def dfs(graph, node, visited):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)

        for neighbor in graph[node]:
            dfs(graph,neighbor,visited)

# visited = set()
# dfs(graph, 'A', visited)
#####################################################################################################

def selection_sort(arr):
    
    for i in range(len(arr)):
        min = i

        for j in range(i+1, len(arr)):
            if arr[j] < arr[min]:
                min = j

        arr[i], arr[min] = arr[min],arr[i]

    print(arr)

arr=[6,7,4,3,2,1]
# selection_sort(arr)
 #####################################################################################################

def job_sheduling(jobs):

    jobs.sort(key=lambda X:X[2],reverse=True)
    max_deadline = max(job[1] for job in jobs)

    slots = [-1] * max_deadline
    total_profit = 0

    for job in jobs:

        for j in range(job[1]-1,-1,-1):
            if slots[j] == -1:
                slots[j] = job[0]
                total_profit += job[2]
                break
    print(slots)
    print(total_profit)

jobs = [
    ("j1",2,100),
    ("j2",1,65),
    ("j3",2,35),
    ("j4",1,10),
    ("j5",3,45)
]
# job_sheduling(jobs)
#####################################################################################################


def is_safe(board,row,col,n):

    for i in range(row):
        if board[i][col] == 1:
            return False

    i,j = row-1,col-1
    while i >= 0 and j >= 0:
        if board[row][col] == 1:
            return False
        i-=1
        j-=1

    i,j = row-1,col+1
    while i >= row and j<n:
        if board[row][col] == 1:
            return False
        i-=1;
        j+=1;

    return True

def queen(board,row,n):
    if row == n:
       print_board(board,n)
       return True

    for col in range(n):
       if is_safe(board,row,col,n):
           
           board[row][col] = 1

           if queen(board, row+1, n):
               return True
           
           board[row][col] =0
    return False


def print_board(board,n):
    for i in range(n):
        for j in range(n):
            print(board[i][j],end=" ")
        print()

n=4
board=[[0] * n for i in range(n)]
# queen(board,0,n)
#####################################################################################################

