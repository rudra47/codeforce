n = 2 * 2
array = sorted([1, 1, 2, 1])

result = 0

for i in range(n):
    prevIndex = i
    i = i + 1
    if array[prevIndex] <= array[i]:
        result += array[prevIndex]

print(result)