# Robot Traversal using Graph Coloring
# Constraint Satisfaction Problem (CSP)

# Graph representing robot locations
graph = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D"],
    "D": ["B", "C", "E"],
    "E": ["D"]
}

# Number of colors
num_colors = 3

# Store color assigned to each location
colors = {node: 0 for node in graph}


# Check whether a color can be assigned
def is_safe(node, color):
    for neighbour in graph[node]:
        if colors[neighbour] == color:
            return False
    return True


# Backtracking algorithm
def graph_coloring(nodes, index):

    # All nodes are colored
    if index == len(nodes):
        return True

    node = nodes[index]

    # Try each available color
    for color in range(1, num_colors + 1):

        if is_safe(node, color):

            colors[node] = color

            # Recursively color the next node
            if graph_coloring(nodes, index + 1):
                return True

            # Backtrack
            colors[node] = 0

    return False


# Solve the problem
nodes = list(graph.keys())

if graph_coloring(nodes, 0):

    print("Robot Traversal using Graph Coloring")
    print("------------------------------------")

    for node in nodes:
        print("Location", node, "-> Color", colors[node])

else:
    print("No valid coloring possible.")