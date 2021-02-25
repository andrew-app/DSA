arr = [-9, -9, -9, 1, 1, 1], [0, -9, 0, 4, 3, 2], [-9, -9, -9, 1, 2, 3], [0, 0, 8, 6, 6, 0], [0, 0, 0, -2, 0, 0], [0, 0, 1, 2, 4, 0]

sumarr = [],[],[],[]


for o in range(0, 4):
    for p in range(0, 4):
        sumarr[o].append(0)



def sumRange(L,x,y,index):
    t = 0
    for f in range(x,y):
        t += L[index][f]

    return t

def sumRangeM(L, index, j):

    m = L[index][j]

    return m





for i in range(0, 4):
    a = 0

    b = 3

    c = 1




    for j in range(0, 4):
        top = sumRange(arr, a, b, i)

        mid = sumRangeM(arr, i+1, c)

        bot = sumRange(arr, a, b, i+2)

        a += 1
        b += 1
        c += 1

        sumarr[i][j] = top + mid + bot



maxval = sumarr[0][0]
for k in range(0,4):
    if max(sumarr[k]) >= maxval:
        maxval = max(sumarr[k])

print(maxval)



