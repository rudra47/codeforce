for _ in range(int(input())):
    n = int(input())
    array = sorted(list(map(int, input().split())))

    poligone = 0
    result = 0
    base = 0
    prev = 0

    for i in range(n):
        if base == array[i]:
            poligone += 1
        else:
            poligone = 0

        if poligone > 2 and base != prev:
            result += 1
            prev = array[i]

        base = array[i]

    print(result)