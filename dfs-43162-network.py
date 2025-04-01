def solution(n, computers):
    
    count = 0
    visited = set()
    
    def dfs(node):
        visited.add(node)
        
        for neighbor in range(n):
            if neighbor not in visited and computers[node][neighbor]:
                dfs(neighbor)
    
    for start in range(n):
        if start not in visited:
            dfs(start)
            count += 1
    
    return count