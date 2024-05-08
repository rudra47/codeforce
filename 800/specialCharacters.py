for _ in range(int(input())):
    n= int(input())

    if n % 2 != 0:
        print("NO")
    else:
        str = ''
        print("YES")
        k = n // 2
        for x in range(1, k + 1):
            if x % 2 != 0:
                str += "AA"
            else:
                str += "BB"
        print(str)