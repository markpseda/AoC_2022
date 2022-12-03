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

while(index < size):
    backPack1 = backPacks[index]
    backPack2 = backPacks[index + 1]
    backPack3 = backPacks[index + 2]

    commonBetween1and2 = set()
    for char in backPack1:
        if(char != '\n' and backPack2.find(char) != -1):
            commonBetween1and2.add(char)
    
    for char in commonBetween1and2:
        if(backPack3.find(char) != -1):
            totalSum += get_priority(char)
            break
    index +=3

print(totalSum)