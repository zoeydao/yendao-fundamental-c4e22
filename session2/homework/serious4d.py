# #d. n stars and xs in total (n is entered by users)
n = int(input("Enter number of stars and xs in total"))
for _ in range(int(n/2)):
    print ("x", end="")
    print ("*", end="")
print ("x",end="")