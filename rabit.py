n =input ("How many pairs of rabbits are here? ")
month = input("How many months after? ")

x = [n,n] + [0]*month

for i in range(0, (month-2)):
    x[i+2] = x[i]+x[i+1]
    print x[i], "pairs of rabbits"
print x[month-2], "pairs of rabbits"
print x[month-1], "pairs of rabbits"
