import sys
sys.stdin = open('input.txt')

def dijkstra(arr, n):
    dist = [INF] * (N+1)
    visited = [0] * (N+1)

    dist[n] = 0

    for _ in range(N):
        min_idx = -1
        min_value = INF

        for i in range(N + 1):
            if not visited[i] and min_value > dist[i]:
                min_idx = i
                min_value = dist[i]

        visited[min_idx] = 1

        for i in range(N + 1):
            if not visited[i] and dist[i] > dist[min_idx]+ arr[min_idx][i]:
                dist[i] = dist[min_idx] + arr[min_idx][i]
    return dist


T = int(input())
for tc in range(1, T+1):
    N, M, X = map(int, input().split())
    INF = 100000
    adj1 = [[INF] * (N+1) for _ in range(N+1)]
    adj2 = [[INF] * (N+1) for _ in range(N+1)]

    for i in range(M):
        n1, n2, w = map(int, input().split())
        adj1[n1][n2] = w
        adj2[n2][n1] = w

    max_v = 0
    d1 = dijkstra(adj1, X)
    d2 = dijkstra(adj2, X)

    max_v = 0
    for i in range(1, N+1):
        if d1[i] + d2[i] > max_v:
            max_v = d1[i] + d2[i]

    print('#{} {}'.format(tc, max_v))
