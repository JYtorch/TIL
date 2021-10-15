import sys
sys.stdin = open('input.txt')

edge = list(map(int, input().split()))
V , E = 7, 8

adj = [[0] * (V+1) for _ in range(V+1)]
visited = [0] * (V+1)
for i in range(E):
    n1 = edge[i*2]
    n2 = edge[i*2 + 1]
    adj[n1][n2] = 1
    adj[n2][n1] = 1
print(adj)


def dfs(v):
    visited[v] = 1
    print(v)
    for w in range(V+1):
        if adj[v][w] and not visited[w]:
            dfs(w)

# stack = []
# def dfs2(v):
#
#     stack.append(v)
#     visited[v] = 1
#
#     while stack:
#         v = stack.pop()
#         print(v)
#
#         for w in range(V+1):
#             if adj[v][w] and not visited[w]:
#                 stack.append(w)
#                 visited[v] = 1
#
# dfs2(1)

# print(adj)

# stack = []
# def dfs3(v):
#     stack.append(v)
#
#     while stack:
#         v = stack.pop()
#         # if not visited[v]:
#         print(v)
#         visited[v] = 1
#         for w in range(V+1):
#             if adj[v][w] and not visited[w]:
#                 visited[w] = 1
#                 stack.append(w)
# dfs3(1)
