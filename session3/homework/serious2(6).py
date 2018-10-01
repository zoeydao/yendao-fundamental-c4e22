#2.5
name = 'Yen'
flock = [5,7,300,90,24,50,75]
month = 4
print('Hello, my name is',name,'and these are my sheep size',flock)

for i in range(1,month):
    biggest = max(flock)
    print("Now my biggest sheep has size",biggest,"let's shear it")
    biggest_size = flock.index(biggest)
    flock[biggest_size] = 8
    print("After shearing, here is my flock",flock)
    for sheep in flock:
        position = flock.index(sheep)
        sheep += 50
        flock[position] = sheep
    print("Month",i,":")
    print ("One month has passed, now here is my flock",flock)
    i +=1
#2.6
total_size = 0
money = 2
for sheep in flock:
    total_size = total_size + sheep
print("My flock has size in total", total_size)
total_money = total_size * money
print("I would get", total_size,"*",money,"$ =",total_money)
