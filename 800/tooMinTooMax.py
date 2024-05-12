# Too Min Too Max
for _ in range(int(input())):
    n = int(input())
    array = sorted(list(map(int, input().split())))

    i = array[n - 1]
    j = array[0]
    k = array[n - 2]
    l = array[1]

    result = abs(i - j) + abs(j - k) + abs(k - l) + abs(l - i)

    print(result)