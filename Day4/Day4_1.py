source = open('input_test.txt')

assignments = source.readlines()

index = 0

size = len(assignments)

numCompleteOverlaps = 0

while(index < size):
   subLists = assignments[index].split(',')
   #print(subLists[0])
   listA = subLists[0].split('-')
   startA = int(listA[0])
   stopA = int(listA[1])
   listB = subLists[1].split('-')
   startB = int(listB[0])
   stopB = int(listB[1])
   #print(startA)
   #print(stopA)
   #print(startB)
   #print(stopB)
   #print()

   if((startA >= startB and startA <= stopB) or (startB >= startA and startB <= stopA)):
       print(subLists[0] + " " + subLists[1])
       numCompleteOverlaps += 1

   index +=1

print(numCompleteOverlaps)