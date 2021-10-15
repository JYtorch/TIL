import sys
sys.stdin = open('input.txt')

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def bfs():
    q = [0] * 100000
    front = rear = -1

    rear += 1
    q[rear] = (0, 0)
    dist[0][0] = 0

    while front != rear:
        front += 1
        r, c = q[front]

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < N and 0 <= nc < N:
                if dist[nr][nc] > dist[r][c] + board[nr][nc]:
                    dist[nr][nc] = dist[r][c] + board[nr][nc]
                    rear += 1
                    q[rear] = (nr, nc)
    return dist[N-1][N-1]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [list(map(int, input())) for _ in range(N)]
    dist = [[987654321] * N for _ in range(N)]

    print('#{} {}'.format(tc, bfs()))