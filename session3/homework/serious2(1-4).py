#2.1
name = 'Yen'
flock = [5,7,300,90,24,50,75]
print('Hello, my name is',name,'and these are my sheep size',flock)
#2.2
biggest = max(flock)
print("Now my biggest sheep has size",biggest,"let's shear it")
#2.3
biggest_size = flock.index(biggest)
flock[biggest_size] = 8
print("After shearing, here is my flock",flock)
#2.4
for sheep in flock:
    position = flock.index(sheep)
    sheep += 50
    flock[position] = sheep
print ("One month has passed, now here is my flock",flock)
