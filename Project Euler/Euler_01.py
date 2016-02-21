# Euler01 - Calculator to solve the sum of multiple of 3 and 5 below 1000
myList = []

x = 1
while x < 1000:
    if x%3 != 0:
        if x%5 != 0:
            x += 1
        else:
            myList.append(x)
            x += 1
    else:
        myList.append(x)
        x += 1

print (myList)

acc = 0
for i in myList:
  acc += i
print ("Answer is: %d" % acc)
