import sys
sys.stdin = open('input.txt')

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


# 선택하기
def select(k, cursum, board):
    global ans
    if cursum == number:
        ans = cursum
        return
    if k == N:
        if ans < cursum:
            ans = cursum
        return
    for w in range(W):
        board2 = [arr[:] for arr in board]

        h = 0
        while h < H and not board[h][w]: h += 1
        if h >= H: continue


        tmp = shot(h, w, board2)
        sort_board(board2)
        select(k + 1, cursum + tmp, board2)


# 터뜨리기
def shot(i, j, board):
    Q = [(i, j, board[i][j])]
    board[i][j] = 0
    cnt = 1
    while Q:
        r, c, value = Q.pop(0)
        for i in range(1, value):
            for d in range(4):
                nr, nc = r + i * dr[d], c + i * dc[d]
                if 0 <= nr < H and 0 <= nc < W and board[nr][nc]:
                    if board[nr][nc] > 1:
                        Q.append((nr, nc, board[nr][nc]))
                    board[nr][nc] = 0
                    cnt += 1
    return cnt


# 정렬하기
def sort_board(board):
    for w in range(W):
        tmp_h = H - 1
        for h in range(H - 1, -1, -1):
            if board[h][w]:
                if tmp_h != h:
                    board[tmp_h][w], board[h][w] = board[h][w], board[tmp_h][w]
                tmp_h -= 1


for T in range(1, int(input()) + 1):
    N, W, H = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(H)]
    number = 0
    for lst in arr:
        for num in lst:
            if num:
                number += 1
    ans = 0
    select(0, 0, arr)
    print('#{} {}'.format(T, number - ans))