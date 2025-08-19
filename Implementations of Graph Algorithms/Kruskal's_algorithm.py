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
    print(parent)
    rank = [0] * n
    min_weight = 0
    for edge in edges:
        u = find_parent(parent, edge[0])
        v = find_parent(parent, edge[1])
        wt = edge[2]
        if u != v:
            min_weight += wt
            union_set(u, v, parent, rank)
    return min_weight,parent

edges = [
    [0, 1, 10],
    [0, 2, 6],
    [0, 3, 5],
    [1, 3, 15],
    [2, 3, 4]
]
n = 4

print(minimum_spanning_tree(edges, n))  
  



# to handle the alphabetical nodes 

# we  make the list of each nodes

# done = []
# alphanodes ={}
#   for node in nodes:
#     if node[0] not in done:
#         alphanodes[i] = [0]   
#         done.append(node[0])
#     if node[1] not in done:
#         done.append(node[1])
#         alphanodes[i] = [0]    
# def union_set(u, v, parent, alphanodes):
#     u_parent = find_parent(parent, u)
#     v_parent = find_parent(parent, v)
#     if alphanodes.get(u_parent) < alphanodes.get(v_parent):
#         parent[u_parent] = v_parent
#     elif alphanodes.get(v_parent) < alphanodes.get(u_parent):
#         parent[v_parent] = u_parent
#     else:
#         parent[v_parent] = u_parent
#         alphanodes[u_parent ]+= 1


#  the below code is to handle the alphabetical nodes



#   def union_set(u, v, parent, rank):
#     u_parent = find_parent(parent, u)
#     v_parent = find_parent(parent, v)

#     if rank[u_parent] < rank[v_parent]:
#         parent[u_parent] = v_parent
#     elif rank[v_parent] < rank[u_parent]:
#         parent[v_parent] = u_parent
#     else:
#         parent[v_parent] = u_parent
#         rank[u_parent] += 1   # increase rank

#  for u, v, _ in edges:
#         if u not in parent:
#             parent[u] = u
#             rank[u] = 0
#         if v not in parent:
#             parent[v] = v
#             rank[v] = 0

#     min_weight = 0
#     mst_edges = []

#     # Process edges
#     for u, v, wt in edges:
#         u_parent = find_parent(parent, u)
#         v_parent = find_parent(parent, v)

#         if u_parent != v_parent:
#             min_weight += wt
#             mst_edges.append((u, v, wt))
#             union_set(u, v, parent, rank)

#     return min_weight, mst_edges
