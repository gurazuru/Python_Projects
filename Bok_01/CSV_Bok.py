# A program that prints out a table based on two different CSV files
fileInput1 = open('F:\\Library\\Python\\Bok_01\\input1.csv', 'r', encoding = "utf8")
fileInput2 = open('F:\\Library\\Python\\Bok_01\\input2.csv', 'r', encoding = "utf8")

newContent1 = {}
newContent2 = {}
outputList = []

content1 = fileInput1.read()
content1 = content1.split("\n") 

content2 = fileInput2.read()
content2 = content2.split("\n")

#Add elements for dict from input1
for i in range(0, len(content1)):
    content1Elem = content1[i].split(",")
    newContent1[content1Elem[0]] = content1Elem[1]

#Add elements for dict from input2
for i in range(0, len(content1)):
    content2Elem = content2[i].split(",")
    newContent2[content2Elem[0]] = content2Elem[1]

#Match similar values from input1 and input2
for k in newContent1:
    if k in newContent2:
        outputList.append(newContent2[k] + "," + newContent1[k])

print("\n".join(outputList))
