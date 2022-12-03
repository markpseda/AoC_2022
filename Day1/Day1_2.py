thing = open('input.txt')

lines = thing.readlines()

index = 0

size = len(lines)

Calories_1 = 0
Calories_2 = 0
Calories_3 = 0
currentCalories = 0

while(index < size):
    if(lines[index] == '\n'):
        if(currentCalories < Calories_3):
            currentCalories = 0
            index += 1
            continue
        elif(currentCalories >= Calories_1):
            Calories_3 = Calories_2
            Calories_2 = Calories_1
            Calories_1 = currentCalories
        elif(currentCalories >= Calories_2):
            Calories_3 = Calories_2
            Calories_2 = currentCalories
        elif(currentCalories >= Calories_3):
            Calories_3 = currentCalories
        currentCalories = 0
        index += 1
        continue

    calories = int(lines[index])
    currentCalories += calories
    index += 1

print(Calories_1 + Calories_2 + Calories_3)