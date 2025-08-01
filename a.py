import math
from queue import PriorityQueue
def INITIALIZE_SINGLE_SOURCE(G,s):
    cost = dict()
    prev = dict()
    for vertex in G.keys():
        cost[vertex] = math.inf
        prev[vertex] = " "
    cost[s]= 0
    return cost,prev

# from queue import PriorityQueue
# PQ = PriorityQueue
# PQ.put((2,"A"))
# PQ.put((1,"B"))
# PQ.PUT((3,"C"))
# while (not PQ.empty()):




G = {
    's':{'t':10 ,'y':5},

    't':{'y': 2 ,'x' :1},
    'x':{'z' : 4},
    'y':{"z":2, "x":9,"t":3},
    'z':{"x":6,"s":7}
}
def INITIALIZE_SINGLE_SOURCE(G,s):
    cost = dict()
    prev = dict()
    for vertex in G.keys():
        cost[vertex] = math.inf
        prev[vertex] = " "
    cost[s]= 0
    return cost,prev


def RELAX(G,u,v,cost,prev):
    if cost[v] >cost[u] +G[u][v]:
        cost[v]= cost[u]+G[u][v]
        prev[v] = u
    return cost,prev    


def DJ(G,s):
    cost,prev = INITIALIZE_SINGLE_SOURCE(G,s)
    PQ = PriorityQueue()
    # PQ.put((2,"A"))
    # PQ.put((1,"B"))
    # PQ.PUT((3,"C"))
    for vertex in G.keys():
        PQ.put((cost[vertex], vertex))
    visited = []
    while (len(visited) != len(G.keys())):
        _, currentVertex = PQ.get()
        visited.append(currentVertex)
        for chimeki in G[currentVertex].keys():
            if chimeki not in visited:
                cost, prev = RELAX(G, currentVertex, chimeki, cost, prev)
            # PQ.put((cost[chimeki],chimeki))
    return cost, prev    

# s = "s"
# cost,prev = DJ(G,s)
# print(cost)
# print(prev)



    
def RECONSTRUCT_PATH(vertex, prev):
    path = vertex
    while prev[vertex ] != " ":
        path  = prev[vertex] + "->" + path
        vertex = prev[vertex]

    return path
s = "t"
cost,prev = DJ(G,s)    
for vertex in G.keys():
    print(f"shortest path from {s} to {vertex} is {RECONSTRUCT_PATH(vertex,prev)}")
    print(f"cost is {cost[vertex]}")


