# Contest Proposal
for _ in range(int(input())):
    t = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    # a = sorted([4, 5, 6, 7, 8, 9])
    # b = sorted([1, 2, 3, 4, 5, 6])

    result = 0

    for i in range(len(a)):
        if a[i] > b[i]:
            a.insert(i, b[i])
            a.sort()
            result += 1

    print(result)