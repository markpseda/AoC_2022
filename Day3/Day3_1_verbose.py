backPacksSource = open('input.txt')

backPacks = backPacksSource.readlines()

index = 0

size = len(backPacks)

totalSum = 0

def get_priority(val):
    if(ord(val) >= ord('a') and ord(val) <= ord('z')):
        return ord(val) - 96
    else:
        return ord(val) - 38

#print(get_priority('a'))
#print(get_priority('z'))
#print(get_priority('A'))
#print(get_priority('Z'))

while(index < size):
    #print(rounds[indeX])
    compartment1 = backPacks[index][0:int((len(backPacks[index])/2))]
    compartment2 = backPacks[index][int((len(backPacks[index])/2)):]

    for char in compartment1:
        if(compartment2.find(char) != -1):
            totalSum += get_priority(char)
            break


    #print(compartment1)
    #print(compartment2)
    index += 1



print(totalSum)