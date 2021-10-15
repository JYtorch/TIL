import sys
sys.stdin = open('input.txt')
from collections import deque

def bfs(n, t):

    q = deque()
    q.append((n, 0))

    used = set()
    while q:
        n, cnt = q.popleft()

        if n in used: continue
        used.add(n)
        if n == t:
            return cnt

        if 0 < n+1 <= 1000000:
            q.append((n+1, cnt + 1))

        if 0 < n*2 <= 1000000:
            q.append((n*2, cnt + 1))

        if 0 < n-1 <= 1000000:
            q.append((n-1, cnt + 1))

        if 0 < n-10 <= 1000000:
            q.append((n-10, cnt+1))



T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    ans = 999999

    print('#{} {}'.format(tc, bfs(N, M)))

