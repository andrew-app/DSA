import time
start_time = time.time()
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
colors = []

pairs = {}

count = 0
i = 0
for x in ar: # identify each color
    if x not in colors:
        colors.append(x)

for y in colors:  # add to hash table
    pairs[y] = 1

for j in ar:  # count for each sock color
    if i != ar.index(j):
        pairs[j] += 1
    i += 1

for a in pairs:  # calculate no. of pairs
    pairs[a] = pairs[a]//2

for b in pairs:  # overall no. of pairs
    count += pairs[b]

print(count)

print("--- %s seconds ---" % (time.time() - start_time))


#pairs = sum(ar.count(i)//2 for i in set(ar))

