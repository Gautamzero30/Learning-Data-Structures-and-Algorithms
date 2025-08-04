import math
d = {
    "a":{"b": 1,"d" : 4},
    "b":{"c ":3,"e":3},
    "c":{"f":2,"e":2},
    "d":{"e":5},
    "e":{"f":4}

}

def validate(u,v,g,prev,cost, min):
    prev[v]=u
    cost[v] = min




def build(d,s):
    prev ={}
    cost = {}
    for i in d.keys():
        prev[i] = " "
        cost[ i] = 0
    now = s
    visited = []
    visited.append(now)
    while len(visited) != len(d.keys()):
        min = math.inf
        for ximeke in d[now].keys():
            if d[now][ximeke] <= min:
                min = d[now][ximeke]
                pencil = ximeke
            validate(now,pencil,d,prev,cost,min)
        now = pencil
        visited.append(pencil)

    print(prev)
    print(cost)
if __name__ =="__main__":    
    S = "a"    
    build(d,S)

 # cost,prev