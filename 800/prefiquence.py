# Prefiquence
for _ in range(int(input())):
    t = list(map(int, input().split()))
    m = input()
    n = input()

    i = 0
    j = 0

    while(i < len(m) and j < len(n)):
        if(m[i] == n[j]):
            i = i + 1
            j = j + 1
        else:
            j = j + 1

    print(i)