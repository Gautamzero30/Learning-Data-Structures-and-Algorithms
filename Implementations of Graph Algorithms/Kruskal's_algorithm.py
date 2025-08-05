def find_parent(parent, node):
    if parent[node] != node:
        parent[node] = find_parent(parent, parent[node])
    return parent[node]

def union_set(u, v, parent, rank):
    u_parent = find_parent(parent, u)
    v_parent = find_parent(parent, v)
    if rank[u_parent] < rank[v_parent]:
        parent[u_parent] = v_parent
    elif rank[v_parent] < rank[u_parent]:
        parent[v_parent] = u_parent
    else:
        parent[v_parent] = u_parent
        rank[u_parent] += 1

def get_weight(edge):
    return edge[2]

def minimum_spanning_tree(edges, n):
    edges.sort(key=get_weight)
    parent = [i for i in range(n)]
    rank = [0] * n
    min_weight = 0
    for edge in edges:
        u = find_parent(parent, edge[0])
        v = find_parent(parent, edge[1])
        wt = edge[2]
        if u != v:
            min_weight += wt
            union_set(u, v, parent, rank)
    return min_weight

edges = [
    [0, 1, 10],
    [0, 2, 6],
    [0, 3, 5],
    [1, 3, 15],
    [2, 3, 4]
]
n = 4

print(minimum_spanning_tree(edges, n))  
