source = open('input_test.txt')

message = source.readline()

i = 0

size = len(message)

distinct = list()
while(i < size):

    distinct.append(message[i])

    finished = True
    if(len(distinct) == 14):
        for a in range(0, 3):
            if(distinct.count(distinct[a]) != 1):
                finished = False

    if finished and len(distinct) == 14:
        print(i)
        break
    
    if(len(distinct) == 14):
        distinct.pop(0)

    i += 1