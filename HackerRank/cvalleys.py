path = 'UDDDUDUU'

pos = 0

valleys = 0

for x in path:
    if x == "U":
        pos += 1

    elif x == "D":
        pos -= 1

    if pos == 0:
        if x == "U":
            valleys += 1

print(valleys)

