#Euler02 - Calculator to calculate the sum of even fibonacci numbers up to 4000000
fibonacciList = [1, 1]
fibonacciEven = []

x = 1
y = 1
z = 0
max = 4000000
while z < max:
    z = x+y
    fibonacciList.append(z)
    x = y
    y = z

fibonacciSum = 0
for i in range(len(fibonacciList)):
    if fibonacciList[i] % 2 == 0:
        fibonacciSum += fibonacciList[i]

print ("fibonacci numbers are: %s" % fibonacciList)
print ("sum of even fibonacci numbers up to %s is %d" % (max, fibonacciSum))
