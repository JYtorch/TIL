import sys
sys.stdin = open('input.txt')

dr = [1, 1, -1, -1]
dc = [-1, 1, 1, -1]

def dfs(r, c, direction, desert, cursum):
    global ans

    if len(desert) >= 4 and (r-1, c-1) == (i, j) and visited[i+1][j-1]:
        if ans < cursum:
            ans = cursum + 1
        return
    else:
        for k in range(4):
            if k == direction or k == direction + 1:
                nr = r + dr[k]
                nc = c + dc[k]
                if nr < 0 or nr >= N or nc < 0 or nc >= N: continue
                if visited[nr][nc] or arr[nr][nc] in desert: continue
                visited[nr][nc] = 1
                dfs(nr, nc, k, desert + [arr[nr][nc]], cursum + 1)
                visited[nr][nc] = 0



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    desert = []
    ans = -1
    for i in range(N):
        for j in range(N):
            dfs(i, j, 0, [arr[i][j]], 0)

    print('#{} {}'.format(tc, ans))

# def solution(r, c, dir, l):
#
#     if dir == 3 and (si, sj) == (r + dr[3], c + dc[3]):
#         return
#
#
#
#     if dir == 0:
#         solution(r + dr[0], c + dc[0], 0, l + 1)
#         solution(r + dr[1], c + dc[1], 1, l + 1)
#
#
#     elif dir == 1:
#         solution(r + dr[1], c + dc[1], 1, l + 1)
#         solution(r + dr[2], c + dc[2], 2, l + 1)
#
#
#     elif dir == 2:
#         if si - sj == r - c:
#             solution(r + dr[3], c + dc[3], 3, l + 1)
#         else:
#             solution(r + dr[2], c + dc[2], 2, l + 1)
#
#     else:
#         solution(r + dr[3], c + dc[3], 3, l + 1)






# dr = [1, 1, -1, -1]
# dc = [1, -1, -1, 1]
# # state = 0 : 우하
# # state = 1 : 좌하
# # state = 2 : 좌상
# # state = 3 : 우상
#
# def find(r, c, cursum, desert, state):
#     global ans
#
#     if len(desert) >= 4 and visited[i+1][j-1] and (r-1, c+1) == (i, j):
#         if ans < cursum:
#             ans = cursum
#         return
#     else:
#         for k in range(4):
#             if k != state and k != state + 1:  continue
#             nr = r + dr[k]
#             nc = c + dc[k]
#             if nr < 0 or nr >= N or nc < 0 or nc >= N or visited[nr][nc]: continue
#             if (nr, nc) == (0, 0) or (nr, nc) == (0, N-1) or (nr, nc) == (N-1, 0) or (nr, nc) == (N-1, N-1): continue
#             if cafe[nr][nc] in desert: continue
#             visited[nr][nc] = 1
#             find(nr, nc, cursum + 1, desert + [cafe[nr][nc]], k)
#             visited[nr][nc] = 0
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     cafe = [list(map(int, input().split())) for _ in range(N)]
#     visited = [[0] * N for _ in range(N)]
#     ans = -1
#
#     for i in range(N):
#         for j in range(N):
#             if j == 0 or j == N-1 or i > N-2: continue
#             visited[i][j] = 1
#             find(i, j, 1, [cafe[i][j]], 0)
#             visited[i][j] = 0
#     print('#{} {}'.format(tc, ans))