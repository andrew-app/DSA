arr = [1,2,3,4,5]

d = 2

n = 7



def rotleft(a,d):
    return a[d:] + a[:d]




print(rotleft(arr,d))