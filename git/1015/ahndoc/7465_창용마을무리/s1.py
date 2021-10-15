import sys
sys.stdin = open('input.txt')

def findset(x):
    while P[x] != x:
        x = P[x]
    return x

def bfs(n):
    q = [0] * 100000
    front = rear = -1

    rear += 1
    q[rear] = n
    visited[n] = 1

    while front != rear:
        front += 1
        v = q[front]

        for u in range(N+1):
            if not visited[u] and adj[v][u]:
                visited[u] = 1
                rear += 1
                q[rear] = u

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    adj = [[0] * (N+1) for _ in range(N+1)]
    P = list(range(N+1))
    for i in range(M):
        n1, n2 = map(int, input().split())
        adj[n1][n2] = adj[n2][n1] = 1
    visited = [0] * (N + 1)
    ans = 0
    for i in range(1, N+1):
        if not visited[i]:
            bfs(i)
            ans += 1
    print('#{} {}'.format(tc, ans))