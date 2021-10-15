import sys
sys.stdin = open('input.txt')
from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    road = [list(map(int, input().split())) for _ in range(N)]
    INF = 10000
    visited = [[INF] * N for _ in range(N)]


    q = deque()
    q.append((0, 0))
    visited[0][0] = 0

    while q:
        r, c = q.popleft()
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]

            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                dif = max(road[nr][nc] - road[r][c], 0)
                if visited[nr][nc] > visited[r][c] + dif + 1:
                    visited[nr][nc] = visited[r][c] + dif + 1
                    q.append((nr, nc))
    print(visited[N-1][N-1])

