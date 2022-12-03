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

    if(oppPlay == 'A'): #rock
        if(myPlay == 'X'): #lose
            #my play is a scissors +3 + 0 
            currentScore += 3
        if(myPlay == 'Y'): #tie
            #my play is a rock +1 + 3 
            currentScore += 4
        if(myPlay == 'Z'): #win
            #my play is a Paper +2 + 06
            currentScore += 8

    if(oppPlay == 'B'): #paper
        if(myPlay == 'X'): #lose
            #my play is a rock +1 + 0 
            currentScore += 1
        if(myPlay == 'Y'): #tie
            #my play is a paper +2 + 3 
            currentScore += 5
        if(myPlay == 'Z'): #win
            #my play is a scissors +3 + 06
            currentScore += 9

    if(oppPlay == 'C'): #scissors
        if(myPlay == 'X'): #lose
            #my play is a paper +2 + 0 
            currentScore += 2
        if(myPlay == 'Y'): #tie
            #my play is a scissors +3 + 3 
            currentScore += 6
        if(myPlay == 'Z'): #win
            #my play is a rock +1 + 06
            currentScore += 7
        
    #print("SZore for round: " + str(currentScore))
    totalScore += currentScore
    #print(totalScore)
    currentScore = 0
    index += 1
    #print()

print(totalScore)


