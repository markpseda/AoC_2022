source = open('input.txt')

crateStuf = source.readlines()

index = 0

size = len(crateStuf)

numCompleteOverlaps = 0

stack1 = list() 
stack2 = list() 
stack3 = list() 
stack4 = list() 
stack5 = list() 
stack6 = list() 
stack7 = list() 
stack8 = list() 
stack9 = list() 


while(crateStuf[index][1] != '1'):
    if(crateStuf[index][0] == '['):
        stack1.insert(0, crateStuf[index][1])
    if(crateStuf[index][4] == '['):
        stack2.insert(0, crateStuf[index][5])
    if(crateStuf[index][8] == '['):
        stack3.insert(0, crateStuf[index][9])
    if(len(crateStuf[index]) <= 12):
        index += 1
        continue
    if(crateStuf[index][12] == '['):
        stack4.insert(0, crateStuf[index][13])
    if(crateStuf[index][16] == '['):
        stack5.insert(0, crateStuf[index][17])
    if(crateStuf[index][20] == '['):
        stack6.insert(0, crateStuf[index][21])
    if(crateStuf[index][24] == '['):
        stack7.insert(0, crateStuf[index][25])
    if(crateStuf[index][28] == '['):
        stack8.insert(0, crateStuf[index][29])
    if(crateStuf[index][32] == '['):
        stack9.insert(0, crateStuf[index][33])
    index += 1


print(stack1)
print(stack2)
print(stack3)
print(stack4)
print(stack5)
print(stack6)
print(stack7)
print(stack8)
print(stack9)


stackIndex = list()
stackIndex.append(stack1)
stackIndex.append(stack2)
stackIndex.append(stack3)
stackIndex.append(stack4)
stackIndex.append(stack5)
stackIndex.append(stack6)
stackIndex.append(stack7)
stackIndex.append(stack8)
stackIndex.append(stack9)

index += 1

while(index < size):
   moveSplit = crateStuf[index].split("from")
   #print(moveSplit)


   numberSplit = moveSplit[0]
   justNumber = numberSplit.split(' ')
   numberToMove = int(justNumber[1])

   otherSplit = moveSplit.pop()
   locs = otherSplit.split(" to ")
   #print("locs" )
   #print(locs)
   toLoc = int(locs.pop())
   fromLoc = int(locs.pop())
   #print(numberToMove)

   fromLoc -= 1
   toLoc -= 1

   #print(fromLoc)
   #print(toLoc)
   #print()

   movables = list()
   for i in range(0,numberToMove):
       movables.insert(0, stackIndex[fromLoc].pop())

   print(movables)

   for elem in movables:
      stackIndex[toLoc].append(elem)
   
   index +=1

print(stack1)
print(stack2)
print(stack3)
print(stack4)
print(stack5)
print(stack6)
print(stack7)
print(stack8)
print(stack9)


stringRes = ""

if(len(stack1) > 0):
    stringRes += stack1.pop()

if(len(stack2) > 0):
    stringRes += stack2.pop()

if(len(stack3) > 0):
    stringRes += stack3.pop()

if(len(stack4) > 0):
    stringRes += stack4.pop()

if(len(stack5) > 0):
    stringRes += stack5.pop()

if(len(stack6) > 0):
    stringRes += stack6.pop()

if(len(stack7) > 0):
    stringRes += stack7.pop()

if(len(stack8) > 0):
    stringRes += stack8.pop()

if(len(stack9) > 0):
    stringRes += stack9.pop()


print(stringRes)