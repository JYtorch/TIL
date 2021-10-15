import sys
sys.stdin = open('input.txt')


def dfs(v, l):
    global ans

    visited[v] = 1

    for u in range(N+1):
        if adj[v][u] and not visited[u]:
            dfs(u, l+1)

    else:
        if ans < l:
            ans = l
        visited[v] = 0
        return

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    adj = [[0] * (N+1) for _ in range(N+1)]
    visited = [0] * (N+1)
    ans = 0
    for _ in range(M):
        n1, n2 = map(int, input().split())
        adj[n1][n2] = 1
        adj[n2][n1] = 1
    for i in range(1, N+1):
        dfs(i, 1)

    print('#{} {}'.format(tc, ans))
