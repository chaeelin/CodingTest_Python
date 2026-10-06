from collections import deque

def solution(board):
    n = len(board)
    m = len(board[0])
    visited = [[False] * m for _ in range(n)]
    distance = [[0] * m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if board[i][j] == "R":
                stx = i
                sty = j
            elif board[i][j] == "G":
                enx = i
                eny = j
                
    def bfs(sx,sy):
        
        queue = deque([(sx,sy)])
        
        while queue:
            x, y = queue.popleft()
            visited[x][y] = True
            
            for dx, dy in ((-1,0), (1,0), (0,1), (0,-1)):
                nx = x
                ny = y
            
                while (0 <= nx+dx < n and 0 <= ny+dy < m) and board[nx+dx][ny+dy] != "D":
                    nx = nx + dx
                    ny = ny + dy
                
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    distance[nx][ny] = distance[x][y] + 1
                    queue.append((nx,ny))
                
                if visited[enx][eny]:
                    return distance[enx][eny]
                
    bfs(stx,sty)

    if distance[enx][eny] > 0:
        return distance[enx][eny]
    else:
        return -1
                