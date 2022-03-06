import sys
sys.stdin = open('input.txt')
from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
def exec_cleaner(position_list):

    q = deque()
    visited = [[0] * C for _ in range(R)]

    for r, c in position_list:

        next_pos = []
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if nr < 0 or nr >= R or nc < 0 or nc >= C or board[nr][nc] == -1 or board[nr][nc] == 0: continue
            next_pos.append((nr, nc))
        if len(next_pos) == 0: continue
        print(next_pos)
        # r, c 좌표에서 상하좌우로 미세먼지 확산
        visited[r][c] += board[r][c] - (board[r][c] // 5) * len(next_pos)
        for y, x in next_pos:
            visited[y][x] += visited[r][c] // 5



    print('--------------')
    for v in visited:
        print(v)


R, C, T = map(int, input().split())
board = []
dust_pos = []
for i in range(R):
    tmp = list(map(int, input().split()))
    board.append(tmp)
    for j in range(C):
        if tmp[j] != 0 and tmp[j] != -1:
            dust_pos.append((i, j))



# for b in board:
#     print(b)
print(R, C, T)
print(dust_pos)
for _ in range(T):
    exec_cleaner(dust_pos)

