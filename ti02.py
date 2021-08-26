a = int(input())
b = int(input())

tot = a
i = 1
n = 0
while i < b:
    tot += a
    i += 1
    while i < n:
        tot = b
        tot = (tot + b)
        i += 1

print(tot)



