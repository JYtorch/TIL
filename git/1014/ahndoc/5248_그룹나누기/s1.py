import sys
sys.stdin = open('input.txt')

def find_set(x):
    while x != p[x]:  # 대표원소가 아니면
        x = p[x]   # x가 가리키는 정점으로 이동
    return x

def union(x, y):
    p[find_set(y)] = find_set(x)

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))

    p = [i for i in range(N + 1)]
    # print(p)
    for i in range(M):
        n1, n2 = data[i*2], data[i*2+1]
        union(n1, n2)

    result = []
    for i in range(N+1):
        result.append(find_set(i))
    # print(result)
    print('#{} {}'.format(tc, len(set(result))-1))

# for tc in range(1, int(input())+1):
#     N, M = map(int, input().split())
#     lst = list(map(int, input().split()))
#     # print(lst)
#     linked = [[] for _ in range(N+1)]
#     visited = [0] * (N+1)
#     for i in range(M):
#         linked[lst[2*i]].append(lst[2*i+1])
#         linked[lst[2 * i+1]].append(lst[2 * i])
#     # print(linked)
#
#     cnt = 0
#     for i in range(1, N+1):
#         if visited[i] == 0:
#             cnt += 1
#             q = [i]
#             while q:
#                 v = q.pop()
#                 for j in linked[v]:
#                     if visited[j] == 0:
#                         visited[j] = 1
#                         q.append(j)
#     print(cnt)
