arr = [1,2,3,4,5]

q = [1,3,2,5,4]

bribes = 0

double = False
for x in arr:
    a = q.index(x)

    b = arr.index(x)

    print(a,b)
    if a != b and double == False:
        if b-a < -2 or b-a > 2:
            print("too chaotic")
        

        bribes += 1
        double = True

    


print(bribes)