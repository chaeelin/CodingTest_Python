from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    def bfs(start, target):
        q = deque()
        q.append((start[0],start[1], 0))
        visited = [[False] * m for _ in range(n)]
        
        visited[start[0]][start[1]] = True
        
        dx = [1, -1, 0, 0]
        dy = [0, 0, -1, 1]
        
        while q:
            x, y, dist = q.popleft()
            
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maps[nx][ny] != "X":
                    
                    visited[nx][ny] = True
                    q.append((nx,ny, dist + 1))
                    
                    if maps[nx][ny] == target:
                        return dist + 1
                    
        return -1
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] == "S":
                start = (i, j)
            elif maps[i][j] == "L":
                lever = (i,j)

    a = bfs(start,'L')
    b = bfs(lever, 'E')
    
    if a == -1 or b == -1:
        return -1
    
    return a + b