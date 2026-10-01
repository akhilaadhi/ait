# Weather Forecasting using DFS

# Weather graph
graph = {
    "Chennai": ["Bangalore", "Hyderabad"],
    "Bangalore": ["Chennai", "Mysore", "Coimbatore"],
    "Hyderabad": ["Chennai", "Vijayawada"],
    "Mysore": ["Bangalore"],
    "Coimbatore": ["Bangalore"],
    "Vijayawada": ["Hyderabad"]
}

# Weather conditions
weather = {
    "Chennai": "Sunny",
    "Bangalore": "Cloudy",
    "Hyderabad": "Sunny",
    "Mysore": "Rainy",
    "Coimbatore": "Rainy",
    "Vijayawada": "Cloudy"
}


def dfs_forecast(start):
    visited = set()

    # Recursive DFS
    def dfs(city):
        if city in visited:
            return

        visited.add(city)

        print(city, "->", weather[city])

        # Visit neighbouring cities
        for neighbour in graph[city]:
            dfs(neighbour)

    print("\nDFS Weather Traversal:")
    dfs(start)


# Start DFS from Chennai
dfs_forecast("Chennai")