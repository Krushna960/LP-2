# Assignment 3
# Name: Krushna Keshav Garole
# Roll No: C32257


# -------------------------------
# Selection Sort
# -------------------------------

def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap elements
        arr[i], arr[min_index] = arr[min_index], arr[i]

    print("Sorted Array:", arr)


arr = [64, 25, 12, 22, 11]
selection_sort(arr)


# -------------------------------
# Job Scheduling
# -------------------------------

def job_scheduling(jobs):

    # Sort jobs by profit in descending order
    jobs.sort(key=lambda x: x[2], reverse=True)

    max_deadline = max(job[1] for job in jobs)

    slots = [-1] * max_deadline
    total_profit = 0

    for job in jobs:

        # Find free slot
        for j in range(job[1] - 1, -1, -1):

            if slots[j] == -1:
                slots[j] = job[0]
                total_profit += job[2]
                break

    print("Jobs done:", slots)
    print("Total Profit:", total_profit)


jobs = [
    ('J1', 2, 100),
    ('J2', 1, 19),
    ('J3', 2, 27),
    ('J4', 1, 25),
    ('J5', 3, 15)
]

job_scheduling(jobs)


# -------------------------------
# Prim's Algorithm
# -------------------------------

def prim(graph):

    visited = set()

    start = list(graph.keys())[0]
    visited.add(start)

    edges = []
    mst_cost = 0

    while len(visited) < len(graph):

        min_edge = None
        min_cost = float('inf')

        for u in visited:

            for v, cost in graph[u]:

                if v not in visited and cost < min_cost:
                    min_edge = (u, v)
                    min_cost = cost

        u, v = min_edge

        visited.add(v)
        edges.append((u, v, min_cost))

        mst_cost += min_cost

    print("MST Edges:", edges)
    print("Total Cost:", mst_cost)


graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('A', 2), ('C', 1), ('D', 1)],
    'C': [('A', 3), ('B', 1), ('D', 4)],
    'D': [('B', 1), ('C', 4)]
}

prim(graph)


# -------------------------------
# Dijkstra's Algorithm
# -------------------------------

def dijkstra(graph, start):

    dist = {node: float('inf') for node in graph}
    dist[start] = 0

    visited = set()

    while len(visited) < len(graph):

        min_node = None
        min_dist = float('inf')

        # Find minimum distance node
        for node in graph:

            if node not in visited and dist[node] < min_dist:
                min_node = node
                min_dist = dist[node]

        visited.add(min_node)

        # Update distances
        for neighbor, cost in graph[min_node]:

            if dist[min_node] + cost < dist[neighbor]:
                dist[neighbor] = dist[min_node] + cost

    print("Shortest Distances:", dist)


graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

dijkstra(graph, 'A')


# -------------------------------
# Kruskal's Algorithm
# -------------------------------

def find(parent, node):

    if parent[node] == node:
        return node

    return find(parent, parent[node])


def union(parent, u, v):

    root_u = find(parent, u)
    root_v = find(parent, v)

    parent[root_v] = root_u


def kruskal(edges, nodes):

    # Sort edges by weight
    edges.sort(key=lambda x: x[2])

    parent = {node: node for node in nodes}

    mst = []
    cost = 0

    for u, v, w in edges:

        if find(parent, u) != find(parent, v):

            union(parent, u, v)

            mst.append((u, v, w))
            cost += w

    print("MST:", mst)
    print("Total Cost:", cost)


edges = [
    ('A', 'B', 2),
    ('A', 'C', 3),
    ('B', 'C', 1),
    ('B', 'D', 4),
    ('C', 'D', 5)
]

nodes = ['A', 'B', 'C', 'D']

kruskal(edges, nodes)