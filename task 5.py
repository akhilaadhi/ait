import random

# Distance between delivery locations
distance = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

# Parameters
num_cities = 4
num_ants = 10
iterations = 50
alpha = 1       # Pheromone importance
beta = 2        # Distance importance
evaporation = 0.5
pheromone_deposit = 100


# Calculate total route distance
def route_distance(route):
    total = 0

    for i in range(len(route) - 1):
        total += distance[route[i]][route[i + 1]]

    # Return to starting city
    total += distance[route[-1]][route[0]]

    return total


# Select next city using pheromone and distance
def select_next_city(current, unvisited, pheromone):
    probabilities = []

    for city in unvisited:
        pheromone_value = pheromone[current][city] ** alpha
        distance_value = (1 / distance[current][city]) ** beta

        probabilities.append(pheromone_value * distance_value)

    total = sum(probabilities)

    probabilities = [p / total for p in probabilities]

    return random.choices(unvisited, weights=probabilities, k=1)[0]


# Ant Colony Optimization
def ant_colony_optimization():

    # Initialize pheromone
    pheromone = [
        [1 for _ in range(num_cities)]
        for _ in range(num_cities)
    ]

    best_route = None
    best_distance = float("inf")

    for iteration in range(iterations):

        all_routes = []

        # Each ant creates a route
        for ant in range(num_ants):

            start = 0
            route = [start]
            unvisited = list(range(1, num_cities))

            while unvisited:
                current = route[-1]

                next_city = select_next_city(
                    current,
                    unvisited,
                    pheromone
                )

                route.append(next_city)
                unvisited.remove(next_city)

            route_dist = route_distance(route)

            all_routes.append((route, route_dist))

            # Update best route
            if route_dist < best_distance:
                best_distance = route_dist
                best_route = route[:]

        # Evaporate pheromone
        for i in range(num_cities):
            for j in range(num_cities):
                pheromone[i][j] *= (1 - evaporation)

        # Deposit pheromone
        for route, route_dist in all_routes:

            deposit = pheromone_deposit / route_dist

            for i in range(len(route) - 1):
                a = route[i]
                b = route[i + 1]

                pheromone[a][b] += deposit
                pheromone[b][a] += deposit

            # Return edge
            a = route[-1]
            b = route[0]

            pheromone[a][b] += deposit
            pheromone[b][a] += deposit

    return best_route, best_distance


# Run ACO
best_route, best_distance = ant_colony_optimization()

print("ANT COLONY OPTIMIZATION")
print("-----------------------")

print("Best Delivery Route:")

for city in best_route:
    print(chr(65 + city), end=" -> ")

print(chr(65 + best_route[0]))

print("Minimum Distance:", best_distance)