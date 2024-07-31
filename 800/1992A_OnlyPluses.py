for _ in range(int(input())):
    array = sorted(list(map(int, input().split())))

    for i in range(5):
        array[0] += 1
        array.sort()

    print(array[0] * array[1] * array[2])
