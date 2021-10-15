import sys
sys.stdin = open('input.txt')

def prim():

    visited = [0] * N
    key = [9876543219876] * N
    key[0] = 0

    for _ in range(N-1):
        min_idx = 0
        min_v = 9876543219876
        # 최소값 찾기
        for i in range(N):
            if not visited[i] and key[i] < min_v:
                min_idx = i
                min_v = key[i]
        visited[min_idx] = 1

        # 갱신
        for i in range(N):
            if not visited[i] and island_adj[min_idx][i] < key[i]:
                key[i] = island_adj[min_idx][i]

    return round(E * sum(key))


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    E = float(input())

    # island = []
    island_adj = [[9876543219876] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            island_adj[i][j] = ((X[i] - X[j]) ** 2 + (Y[i] - Y[j]) ** 2)

    print('#{} {}'.format(tc, prim()))
