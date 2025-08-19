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

def minimum_spanning_tree(edges):
    edges.sort(key=lambda x: x[2])

    parent = {}
    rank = {}

    for u, v, _ in edges:
        if u not in parent:
            parent[u] = u
            rank[u] = 0
        if v not in parent:
            parent[v] = v
            rank[v] = 0

    min_weight = 0
    mst_edges = []

    for u, v, wt in edges:
        u_parent = find_parent(parent, u)
        v_parent = find_parent(parent, v)

        if u_parent != v_parent:
            min_weight += wt
            mst_edges.append((u, v, wt))
            union_set(u, v, parent, rank)

    return min_weight, mst_edges

edges = [
    ("a", "b", 10),
    ("a", "c", 6),
    ("a", "d", 5),
    ("b", "d", 15),
    ("c", "d", 4)
]

weight, mst = minimum_spanning_tree(edges)
print("mst weight:", weight)
print("mst edges:", mst)
