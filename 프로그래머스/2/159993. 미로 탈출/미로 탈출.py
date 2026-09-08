from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    def bfs(sx,sy,target):        
        visited = [[False] * m for _ in range(n)]
        distance = [[0] * m for _ in range(n)]
        
        queue = deque([(sx,sy)])
        visited[sx][sy] = True
        distance[sx][sy] = 0
    
        while queue:
            x,y = queue.popleft()
            
            for dx,dy in ((-1,0), (1,0), (0,1), (0,-1)):
                nx = x + dx
                ny = y + dy
                
                if 0 <= nx < n and 0 <= ny < m:
                    if not visited[nx][ny] and maps[nx][ny] != "X":
                        visited[nx][ny] = True
                        distance[nx][ny] = distance[x][y] + 1
                    
                        if maps[nx][ny] == target:
                            return distance[nx][ny]
                    
                        queue.append((nx,ny))
        return -1
    
    left = -1
    right = -1
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] == "S":
                left = bfs(i,j,"L")
            if maps[i][j] == "L":
                right = bfs(i,j,"E")

    if left == -1 or right == -1:
        return -1
    
    return left + right