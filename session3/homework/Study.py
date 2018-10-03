#1. A nested list is a list that appears as an element in another list, example:
nestedlist = [2,5,'phone',['dog','cat']]
print(nestedlist[3])
print(nestedlist[3][0])
#2. A list can store both integers and string
print(*nestedlist, sep = ',')