import math
from queue import PriorityQueue
# def INITIALIZE_SINGLE_SOURCE(G,s):
#     cost = dict()
#     prev = dict()
#     for vertex in G.keys():
#         cost[vertex] = math.inf
#         prev[vertex] = " "
#     cost[s]= 0
#     print("aa")
#     return cost,prev

# from queue import PriorityQueue
# PQ = PriorityQueue
# PQ.put((2,"A"))
# PQ.put((1,"B"))
# PQ.PUT((3,"C"))





G = {
    'a':{'b':2 },

    'd':{'b': 11 ,'f' :9},
    'f':{'a' : 7,'c':3,"e":1},
    'c':{"a":6 },
    'e':{"c":5}
}
def INITIALIZE_SINGLE_SOURCE(G,s):
    cost = dict()
    prev = dict()
    for vertex in G.keys():
        cost[vertex] = math.inf
        prev[vertex] = " "
    cost[s]= 0
    print("cc")
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
        print(list(PQ.queue))
    visited = []
    while (len(visited) != len(G.keys())):
        _, currentVertex = PQ.get()
        
        visited.append(currentVertex)
        for chimeki in G[currentVertex].keys():
            if chimeki not in visited:
                print(visited)
                print(list(PQ.queue))
                cost, prev = RELAX(G, currentVertex, chimeki, cost, prev)
                
                
                PQ.put((cost[chimeki],chimeki))
                print(list(PQ.queue))
                print(prev)
                print(cost)
    return cost, prev    

# s = "s"
# cost,prev = DJ(G,s) 
# print(cost)
# print(prev)



    
def RECONSTRUCT_PATH(vertex, prev):
    path = vertex
    while prev[vertex ] != " ":
        print(path)
        path  = prev[vertex] + "->" + path
        vertex = prev[vertex]

    return path
s = "f"
cost,prev = DJ(G,s)    
for vertex in G.keys():
    print(f"shortest path from {s} to {vertex} is {RECONSTRUCT_PATH(vertex,prev)}")
    print(f"cost is {cost[vertex]}")


