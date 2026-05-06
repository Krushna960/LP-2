# Assignment 1
# Name: Krushna Keshav Garole
# Roll No: C32257


# Graph represented using adjacency list (undirected graph)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# BFS (Breadth-First Search)
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


# DFS (Depth-First Search - Recursive)
def dfs(graph, node, visited):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)

        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)


# Main
print("BFS Traversal:")
bfs(graph, 'A')

print("\nDFS Traversal:")
visited = set()
dfs(graph, 'A', visited)