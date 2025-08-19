import heapq

def prim_mst(graph, start_node):
    visited = []
    min_heap = [(0, start_node, None)] # to store the datas in the min heap (weight, current_node, parent)
    total_weight = 0
    mst_edges = []      # to  stores the (parent, node, weight)
    mst_pairs = []      #  to stores just the(parent, node)
    print(f"Initial min_heap: {min_heap}")
    while min_heap:
        weight, node, parent = heapq.heappop(min_heap)
        if node in visited:
            continue

        visited.append(node)
        print(f"Visiting node: {node}, Weight: {weight}, Parent: {parent}")
        total_weight += weight
        
        print( f"the mst pairs is {mst_pairs}") 
        if parent is not None:
            mst_edges.append((parent, node, weight))
            mst_pairs.append((parent, node))  # to add the pair here
        print(f"min_heap before adding neighbors: {min_heap}")
    #   adding the neighbours to the min_heap

        for neighbor, edge_weight in graph[node]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (edge_weight, neighbor, node))
        print(f"min_heap after adding neighbors: {min_heap}")
        show(mst_pairs, mst_edges, total_weight,visited)
    return mst_pairs

def show(mst_pairs, mst_edges, total_weight,visited):
     
    print("MST Edges with weights:")
    for u, v, w in mst_edges:
        print(f"{u} -> {v}, weight = {w}")

    print("\nMST Pairs (just connections):")
    for u, v in mst_pairs:
        print(f"{u} -> {v}")

    print("\nTotal Weight of MST:", total_weight)
    print("\nVisited nodes:", visited)
    


if __name__ == "__main__":    
    
    graph = {
        'A': [('B', 1), ('D', 3)],
        'B': [('A', 1), ('D', 3), ('C', 1)],
        'C': [('B', 1), ('D', 1)],
        'D': [('A', 3), ('B', 3), ('C', 1)]
    }

    mst_pairs = prim_mst(graph, start_node='A')
    print("\nFinal list of MST pairs:", mst_pairs)
