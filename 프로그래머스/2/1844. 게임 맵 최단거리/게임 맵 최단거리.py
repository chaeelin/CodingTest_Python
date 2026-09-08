from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    visited = [[False] * m for _ in range(n)]
    distance = [[0] * m for _ in range(n)]
    
    def bfs(sx,sy):
        queue = deque([(sx,sy)])
        visited[sx][sy] = True
        distance[sx][sy] = 1
        
        while queue:
            x,y = queue.popleft()
            
            for dx, dy in ((-1,0), (1,0), (0,1), (0,-1)):
                nx = x + dx
                ny = y + dy
                
                if 0 <= nx < n and 0 <= ny < m:
                    if not visited[nx][ny] and maps[nx][ny] == 1:
                        visited[nx][ny] = True
                        distance[nx][ny] = distance[x][y] + 1
                        queue.append((nx,ny))
                        
    bfs(0,0)
    
    if distance[n-1][m-1] > 0:
        return distance[n-1][m-1]
    else:
        return -1