

q = [1,2,5,3,4]

bribes = 0

chaos = False

for i in range(len(q)-1,0,-1):
    if q[i] != i+1:
        if i-1 >= 0 and q[i-1] == i+1:
            temp = q[i-1]
            q[i-1] = q[i]
            q[i] = temp
            bribes += 1

        elif i-2 >= 0 and q[i-2] == i+1:
            q[i-2] = q[i-1]
            q[i-1] = q[i]
            q[i] = q[i-2]
            bribes += 2

        else:
            chaos = True


if chaos is True:
    print("Too chaotic")

else:
    print(bribes)




