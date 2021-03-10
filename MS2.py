arr = [1,3,5,2,4,6,7]

'''
swaps = 0
for i in range(0, len(arr)-1):
    maxd = []

    for j in range(i+1, len(arr)):
        diff = arr[i] - arr[j]
        maxd.append(diff)

    maxval = maxd[0]
    for k in maxd:
        if k > maxval:
            maxval = k
    if maxval > 0:
        a = maxd.index(maxval)
        b = a+i+1
        if 0 < b <= len(arr)-1:
            temp = arr[b]
            arr[b] = arr[i]
            arr[i] = temp

            swaps += 1

print(str(swaps))
print(arr)

'''
swaps = 0
n = len(arr)

for idx in range(0, n-1):
    while arr[idx] - 1 != idx:
        ele = arr[idx]
        arr[ele - 1], arr[idx] = arr[idx], arr[ele - 1]
        swaps += 1

print(swaps)

