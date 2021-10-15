import sys
sys.stdin = open('input.txt')
V, E = 7, 8
edge = list(map(int, input().split()))

adj = [[0] * (V+1) for _ in range(V+1)]
visited = [0] * (V+1)
for i in range(E):
    n1 = edge[2*i]
    n2 = edge[2*i+1]
    adj[n1][n2] = 1
    adj[n2][n1] = 1
print(adj)

# def bfs(v):
#     queue = [0] * (V+1)
#     front = -1
#     rear = -1
#
#     rear += 1
#     queue[rear] = v
#     visited[v] = 1
#
#     while front != rear:
#         front += 1
#         t = queue[front]
#         print(t)
#         for u in range(V+1):
#             if adj[t][u] and not visited[u]:
#                 rear += 1
#                 queue[rear] = u
#                 visited[u] = 1
#
# bfs(1)

def bfs2(v):
    q = [0] * (V+1)
    front = -1
    rear = -1

    rear += 1
    q[rear] = v
    visited[v] = 1

    while front != rear:
        front += 1
        t = q[front]
        print(t)

        for u in range(V+1):
            if adj[t][u] and not visited[u]:
                visited[u] = visited[t] + 1
                rear += 1
                q[rear] = u

bfs2(1)
print(visited)



