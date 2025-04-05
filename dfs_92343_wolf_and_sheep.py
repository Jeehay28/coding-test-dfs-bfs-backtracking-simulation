# ✅ Time Complexity: O(2^n)
# ✅ Space Complexity: O(n) // You store the tree as an adjacency list: graph = defaultdict(list)

def solution(info, edges):
    from collections import defaultdict
    # “I want to use defaultdict, which is a dictionary that gives a default value when a key doesn’t exist yet.”
    
    # graph = {}
    # if parent not in graph:
    #     graph[parent] = []
    
    # graph = {
    # 0: [1, 2],
    # 1: [3, 4]
    # }

    graph = defaultdict(list)
     # if graph[parent] didn’t exist yet, it automatically creates an empty list for you.
    
    for parent, child in edges:
        graph[parent].append(child)
        
    max_sheep = 0
        
    def dfs(sheep, wolf, current, possible_nodes):
        nonlocal max_sheep
        # In Python, if you want to modify a variable from an outer (but non-global) scope inside a nested function, you must declare it as nonlocal.
        
        if info[current] == 0:
            sheep += 1
        else:
            wolf += 1
        
        if wolf >= sheep:
            return
        
        max_sheep = max(max_sheep, sheep)
        
        next_nodes = possible_nodes + graph[current]
        # next_nodes = [0] + [1, 2]  # → [0, 1, 2]
        next_nodes.remove(current)
        # next_nodes = [1, 2]
        
        for next_node in next_nodes:
            dfs(sheep, wolf, next_node, next_nodes[:])
            # You copy the next_nodes list ([:] means a shallow copy) and go deeper.

    dfs(0, 0, 0, [0])

    return max_sheep

