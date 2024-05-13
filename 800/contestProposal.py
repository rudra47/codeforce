# Contest Proposal
for _ in range(int(input())):
    t = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    result = 0

    for i in range(len(a)):
        if a[i] > b[i]:
            a.insert(i, b[i])
            a.sort()
            result += 1

    print(result)