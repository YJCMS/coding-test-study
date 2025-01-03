import sys
from collections import deque

m, n = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
queue = deque([])
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
result = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append([i, j])
        
def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append([nx, ny])
            
bfs()
result = 0

for row in graph:
    for cell in row:
        if cell == 0:  # 익지 않은 토마토가 있다면
            print(-1)
            exit(0)
        result = max(result, cell)

print(result - 1)