s = "kmretasscityylpdhuwjirnqimlkcgxubxmsxpypgzxtenweirknjtasxtvxemtwxuarabssvqdnktqadhyktagjxoanknhgilnm"

n = 736778906400

c = ""

if len(s) > 1:
    rem = n % len(s)

    i = 1
    for x in s:

        c += str(x)

        if i >= rem:
            break

        i += 1


total = s.count("a")*(n//len(s)) + c.count("a")

test = c.count("a")
print(total)


print(test)

