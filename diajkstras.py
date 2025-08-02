import heapq

def dijkstra(graph, start):
    # graph is a dict: node -> list of (neighbor, weight)
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # priority queue of (distance, node)
    pq = [(0, start)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        # If this distance is already larger, skip
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            # If found shorter path to neighbor
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

# Example usage:
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

start_node = 'A'
distances = dijkstra(graph, start_node)
print(f"Shortest distances from {start_node}: {distances}")
