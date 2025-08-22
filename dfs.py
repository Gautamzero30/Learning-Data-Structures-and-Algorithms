def dfs_util(node, adj, visited):
    visited[node] = True
    print(node, end=" ")

    for neigh in adj[node]:
        if not visited[neigh]:
            dfs_util(neigh, adj, visited)

def dfs(start, adj, V):
    visited = [False] * V
    dfs_util(start, adj, visited)

# Example
V = 5
adj = {
    0: [1, 4],
    1: [0, 2, 3, 4],
    2: [1, 3],
    3: [1, 2, 4],
    4: [0, 1, 3]
}

print("DFS starting from node 0:")
dfs(0, adj, V)
