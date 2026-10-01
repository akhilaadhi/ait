# A* Algorithm for Map Navigation System

import heapq

# Map represented as a graph
graph = {
    "A": {"B": 4, "C": 2},
    "B": {"A": 4, "C": 1, "D": 5},
    "C": {"A": 2, "B": 1, "D": 8, "E": 10},
    "D": {"B": 5, "C": 8, "E": 2, "F": 6},
    "E": {"C": 10, "D": 2, "F": 3},
    "F": {"D": 6, "E": 3}
}

# Heuristic estimated distance to destination F
heuristic = {
    "A": 10,
    "B": 7,
    "C": 8,
    "D": 4,
    "E": 2,
    "F": 0
}


def a_star(start, goal):
    # Priority queue: (f_cost, city)
    open_list = []
    heapq.heappush(open_list, (0, start))

    # Cost from start to each city
    g_cost = {city: float("inf") for city in graph}
    g_cost[start] = 0

    # Store the previous city
    parent = {city: None for city in graph}

    while open_list:

        f_cost, current = heapq.heappop(open_list)

        # Goal reached
        if current == goal:
            break

        # Explore neighbouring cities
        for neighbour, distance in graph[current].items():

            new_g_cost = g_cost[current] + distance

            if new_g_cost < g_cost[neighbour]:

                g_cost[neighbour] = new_g_cost

                # f(n) = g(n) + h(n)
                f_cost = new_g_cost + heuristic[neighbour]

                heapq.heappush(open_list, (f_cost, neighbour))

                parent[neighbour] = current

    # Reconstruct path
    path = []
    current = goal

    while current is not None:
        path.append(current)
        current = parent[current]

    path.reverse()

    return path, g_cost[goal]


# Starting and destination locations
start = "A"
goal = "F"

path, cost = a_star(start, goal)

print("Map Navigation using A* Algorithm")
print("----------------------------------")
print("Start Location:", start)
print("Destination:", goal)
print("Optimal Path:", " -> ".join(path))
print("Total Distance:", cost)