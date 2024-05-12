for _ in range(int(input())):
    n = int(input())
    array = sorted(list(map(int, input().split())))
    median = ((n + 1) // 2) - 1
    result = 1

    for i in range(median + 1, n):
        if array[median] == array[i]:
            result += 1

    print(result)