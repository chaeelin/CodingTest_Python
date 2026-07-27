from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    dist = [[0] * m for _ in range(n)]
    
    q = deque()
    q.append((0,0))
    dist[0][0] = 1
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if not (0 <= nx < n and 0 <= ny < m):
                continue
            if maps[nx][ny] == 0:
                continue
            if dist[nx][ny] != 0:
                continue
                
            dist[nx][ny] = dist[x][y] + 1
            
            q.append((nx,ny))
            
    return dist[n-1][m-1] if dist[n-1][m-1] != 0 else -1