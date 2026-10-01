# Vehicle Routing using Hill Climbing

# Distance between locations
distance = {
    "A": {"A": 0, "B": 10, "C": 15, "D": 20},
    "B": {"A": 10, "B": 0, "C": 35, "D": 25},
    "C": {"A": 15, "B": 35, "C": 0, "D": 30},
    "D": {"A": 20, "B": 25, "C": 30, "D": 0}
}


# Calculate total distance of a route
def calculate_distance(route):
    total = 0

    for i in range(len(route) - 1):
        total += distance[route[i]][route[i + 1]]

    return total


# Hill Climbing algorithm
def hill_climbing(route):
    current_route = route[:]
    current_distance = calculate_distance(current_route)

    while True:
        best_route = current_route[:]
        best_distance = current_distance

        # Try swapping two locations
        for i in range(1, len(current_route) - 1):
            for j in range(i + 1, len(current_route) - 1):

                new_route = current_route[:]

                # Swap locations
                new_route[i], new_route[j] = new_route[j], new_route[i]

                new_distance = calculate_distance(new_route)

                # Select better route
                if new_distance < best_distance:
                    best_route = new_route
                    best_distance = new_distance

        # If no improvement is possible, stop
        if best_distance >= current_distance:
            break

        current_route = best_route
        current_distance = best_distance

    return current_route, current_distance


# Initial route
route = ["A", "B", "C", "D", "A"]

print("Initial Route:", " -> ".join(route))
print("Initial Distance:", calculate_distance(route))

# Apply Hill Climbing
best_route, best_distance = hill_climbing(route)

print("\nFinal Route:", " -> ".join(best_route))
print("Final Distance:", best_distance)