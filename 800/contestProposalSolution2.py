# Contest Proposal
for _ in range(int(input())):
    t = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    ans = 0
    i = 0

    for el in b:
        if a[i] > el:
            ans += 1
        else:
            i += 1

    print(ans)