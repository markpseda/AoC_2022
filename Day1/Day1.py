thing = open('input.txt')

lines = thing.readlines()

index = 0

size = len(lines)

maxCalories = 0
currentCalories = 0

while(index < size):
    if(lines[index] == '\n'):
        if(currentCalories > maxCalories):
            print("New highest calories: " + str(currentCalories))
            maxCalories = currentCalories

        currentCalories = 0
        index += 1
        continue

    calories = int(lines[index])
    currentCalories += calories
    index += 1

print(maxCalories)