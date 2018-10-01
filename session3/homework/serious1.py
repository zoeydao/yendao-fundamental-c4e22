shop = ['T-shirt','Sweater']
#R
print('Welcome to our shop, what do you want (C, R, U, D)? R')
print("Our items: ",end="")
print(*shop, sep=", ")
#C
print('Welcome to our shop, what do you want (C, R, U, D)? C')
new_item = input("Enter new item: ")
shop.append(new_item)
print("Our items: ",end="")
print(*shop, sep=", ")
#U
print('Welcome to our shop, what do you want (C, R, U, D)? U')
while True:
    position = input("Update position: ")
    if position.isdigit():
        position = int(position)
        if 0 < position <= len(shop):
            new_item = input("New item? ")
            shop[position-1] = new_item
            print("Our items: ",end="")
            print(*shop, sep=", ")
            break
        else:
            print("Position is not in the list")
    else:
        print("Please enter a valid position")
#D
print('Welcome to our shop, what do you want (C, R, U, D)? D')
while True:
    position = input("Delete position: ")
    if position.isdigit():
        position = int(position)
        if 0 < position <= len(shop):
            shop.pop(position-1)
            print("Our items: ",end="")
            print(*shop, sep=", ") 
            break
        else:
            print("Position is not in the list")
    else:
        print("Please enter a valid position")