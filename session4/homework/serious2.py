prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

for k,v in prices.items():
    print(k)
    print("price:",v)
    s = stock[k]
    print("stock:",s)

total = 0
for k,v in prices.items():
    s = stock[k]
    total += s*v
print(total)