from collections import deque

def bfs(start, adj, V):
    visited = [False] * V
    q = deque([start])
    visited[start] = True

    while q:
        node = q.popleft()
        print(node, end=" ")

        for neigh in adj[node]:
            if not visited[neigh]:
                visited[neigh] = True
                q.append(neigh)

# Example
V = 5
adj = {
    0: [1, 4],
    1: [0, 2, 3, 4],
    2: [1, 3],
    3: [1, 2, 4],
    4: [0, 1, 3]
}

print("BFS starting from node 0:")
bfs(0, adj, V)
