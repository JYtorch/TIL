import sys
sys.stdin = open('input.txt')


def find(i, k):
    global ans

    if i == N//2:
        food1 = []
        food2 = []
        for c in range(N):
            if used[c]:
                food1.append(c)
            else:
                food2.append(c)
        total1 = 0
        total2 = 0

        # N//2개 중 2개(m, n)를 뽑는 조합
        for m in range(N//2):
            for n in range(m+1, N//2):
                a = food1[m]
                b = food1[n]
                c = food2[m]
                d = food2[n]
                total1 += arr[a][b] + arr[b][a]
                total2 += arr[c][d] + arr[d][c]
        result = abs(total1 - total2)

        if ans > result:
            ans = result

        return
    else:
        for j in range(k, N):
            if used[j] == 0:
                used[j] = 1
                find(i+1, j+1)
                used[j] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    used = [0] * N
    ans = 99999999

    find(0, 0)

    print('#{} {}'.format(tc, ans))