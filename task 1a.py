from collections import deque

# Stock market graph
# Each stock is connected to related stocks
graph = {
    "TCS": ["INFY", "HCL"],
    "INFY": ["TCS", "WIPRO", "TECHM"],
    "HCL": ["TCS", "TECHM"],
    "WIPRO": ["INFY"],
    "TECHM": ["INFY", "HCL"]
}

# Historical market trend of each stock
trend = {
    "TCS": "UP",
    "INFY": "UP",
    "HCL": "DOWN",
    "WIPRO": "UP",
    "TECHM": "UP"
}


def bfs_prediction(start):
    visited = set()
    queue = deque([start])

    up_count = 0
    down_count = 0

    print("\nBFS Stock Traversal:")

    while queue:
        stock = queue.popleft()

        if stock in visited:
            continue

        visited.add(stock)

        print(stock, "->", trend[stock])

        # Count market trends
        if trend[stock] == "UP":
            up_count += 1
        else:
            down_count += 1

        # Add unvisited neighbouring stocks
        for neighbour in graph[stock]:
            if neighbour not in visited:
                queue.append(neighbour)

    # Simple prediction based on majority trend
    print("\nPrediction:")

    if up_count > down_count:
        print("Market Trend: UP")
    elif down_count > up_count:
        print("Market Trend: DOWN")
    else:
        print("Market Trend: STABLE")


# Start BFS from TCS
bfs_prediction("TCS")