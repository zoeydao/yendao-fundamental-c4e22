#g. nxm stars
n = int(input("Enter the number of stars: "))
m = int(input("Enter the number of lines: "))
for _ in range(m):
    for _ in range (n):
        print ("*",end="")
    print()