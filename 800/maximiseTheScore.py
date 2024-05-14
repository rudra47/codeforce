for _ in range(int(input())):
    n = 2 * int(input())
    array = sorted(list(map(int, input().split())))

    result = 0

    for i in range(n):
        if (i) % 2 == 0:
            result += array[i]

    print(result)