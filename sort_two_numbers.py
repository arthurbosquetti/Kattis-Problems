line = input()
a, b = line.split()
a = int(a)
b = int(b)

if a<=b:
    print("{} {}".format(a,b))
else:
    print("{} {}".format(b,a))
