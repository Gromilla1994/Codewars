# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

number = int(input())
newnum = number

counter = 2
nod = 0

while(counter * counter < number):
    if newnum % counter == 0:
        newnum /= counter
        nod = counter
    else:
        counter += 1
    
if counter > number:
    nod = counter

print(nod)