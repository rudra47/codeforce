for _ in range(int(input())):
    n = int(input())
    array = sorted(list(map(int, input().split())))

    count = 0
    result = 0
    prev = array[0]

    for i in range(n):
        if prev == array[i]:
            count += 1
        else:
            result += count // 3
            count = 1
            prev = array[i]

    result += count // 3

    print(result)
