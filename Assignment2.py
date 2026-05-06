# Assignment 2
# Name: Krushna Keshav Garole
# Roll No: C32257


# Graph (adjacency list with cost)
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('A', 1), ('D', 1), ('E', 5)],
    'C': [('A', 3), ('F', 2)],
    'D': [('B', 1)],
    'E': [('B', 5), ('F', 1)],
    'F': [('C', 2), ('E', 1)]
}

# Heuristic values (estimated cost to goal)
heuristic = {
    'A': 6,
    'B': 4,
    'C': 4,
    'D': 2,
    'E': 2,
    'F': 0   # Goal node
}


def a_star(start, goal):
    open_list = [start]
    closed_list = []

    g = {start: 0}          # Cost from start to node
    parent = {start: start} # To reconstruct path

    while open_list:
        # Find node with lowest f = g + h
        n = None
        for v in open_list:
            if n is None or g[v] + heuristic[v] < g[n] + heuristic[n]:
                n = v

        # If goal is reached
        if n == goal:
            path = []
            while parent[n] != n:
                path.append(n)
                n = parent[n]
            path.append(start)
            path.reverse()

            print("Path found:", path)
            return

        # Move node from open to closed
        open_list.remove(n)
        closed_list.append(n)

        # Check neighbors
        for (neighbor, cost) in graph[n]:
            if neighbor not in open_list and neighbor not in closed_list:
                open_list.append(neighbor)
                parent[neighbor] = n
                g[neighbor] = g[n] + cost

            else:
                if g.get(neighbor, float('inf')) > g[n] + cost:
                    g[neighbor] = g[n] + cost
                    parent[neighbor] = n

                    if neighbor in closed_list:
                        closed_list.remove(neighbor)
                        open_list.append(neighbor)

    print("Path does not exist!")


# Run
a_star('A', 'F')