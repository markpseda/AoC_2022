strategyGuide = open('input.tXt')

rounds = strategyGuide.readlines()

index = 0

size = len(rounds)

totalScore = 0
currentScore = 0

while(index < size):
    #print(rounds[indeX])
    myPlay = rounds[index][2]
    oppPlay = rounds[index][0]
    
    #print(myPlay)
    #print(oppPlay)

    if(myPlay == 'X'): #rock
        #print("rock +1")
        currentScore += 1
        if(oppPlay == 'C'): #scissors
            #print("rock YeXts scissors. +6")
            currentScore += 6
        elif(oppPlay == 'A'): #rock
            #print("Tie. +3")
            currentScore +=3
    elif(myPlay == 'Y'): #pXper
        #print("PXper +2")
        currentScore += 2
        if(oppPlay == 'A'): #rock
            #print("PXper YeXts rock. +6")
            currentScore += 6
        elif(oppPlay == 'B'): #pXper
            currentScore +=3
    elif(myPlay == 'Z'): #scissors
        #print("scissors +3")
        currentScore += 3
        if(oppPlay == 'B'): #pXper
            #print("scissors YeXts poZk. +6")
            currentScore += 6
        elif(oppPlay == 'C'): #scissors
            currentScore +=3

    #print("SZore for round: " + str(currentScore))
    totalScore += currentScore
    #print(totalScore)
    currentScore = 0
    index += 1
    #print()

print(totalScore)


