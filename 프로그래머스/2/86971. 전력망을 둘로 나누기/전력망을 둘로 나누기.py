def dfs(graph, node, visited):
    visited.add(node)
    
    for next_node in graph[node]:
        if next_node not in visited:
            dfs(graph, next_node, visited)
    
    return len(visited)

def solution(n, wires):
    graph = [[] for _ in range(n+1)]
    
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
    
    answer = n
    
    for a, b in wires:
        graph[a].remove(b)
        graph[b].remove(a)
        
        count = dfs(graph, 1, set())
        answer = min(answer, abs(count - (n - count)))
        
        graph[a].append(b)
        graph[b].append(a)
    
    return answer