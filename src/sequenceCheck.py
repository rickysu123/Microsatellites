# check the type of microsatellite, whether pure or interrupted
# parameter is the microsatellite
# returns an array containing correct letter, wrong letter, position, in that order
def checkMicroType(sequence):
    n = 3
    array = [sequence[i:i+n] for i in range(0, len(sequence), n)]
    # splits the sequence every 3 characters^
    temp = [] # for pure microsatellites
    if len(sequence) == 9: # U3L9
        if array[0] == array[1] and array[0] == array[2]: # pure microsatellite
            temp.append("Pure microsatellite")
            return temp
        elif array[0] == array[1] and not array[0] == array[2]: # array[2] wrong
            return checkSequence(array[0],array[2],7)
        elif array[0] == array[2] and not array[0] == array[1]: # array[1] wrong
            return checkSequence(array[0],array[1],4)
        elif array[1] == array[2] and not array[0] == array[1]: # array[0] wrong
            return checkSequence(array[1],array[0],1)
    else: # U3L12
        if array[0] == array[1] and array[0] == array[2] and array[0] == array[3]:
            # pure microsatellite
            temp.append("Pure microsatellite")
            return temp
        elif array[0] == array[1] and array[0] == array[2] and not array[0] == array[3]:
            # array[3] wrong
            return checkSequence(array[0],array[3],10)
        elif array[0] == array[1] and array[0] == array[3] and not array[0] == array[2]:
            # array[2] wrong
            return checkSequence(array[0],array[2],7)
        elif array[0] == array[2] and array[0] == array[3] and not array[0] == array[1]:
            # array[1] wrong
            return checkSequence(array[0],array[1],4)
        elif array[1] == array[2] and array[1] == array[3] and not array[0] == array[1]:
            # array[0] wrong
            return checkSequence(array[1],array[0],1)


# this function checks where the microsatellite is interrupted
# parameters are the correct sequence, the wrong sequence, and the starting position
# for example, if the whole microsatellite was AAGAAGAAC,
# correctSeq == AAG, wrongSeq == AAC, startPos == 7
def checkSequence(correctSeq, wrongSeq, startPos):
    count = 0
    tempArray = [] # keep track of right letter, wrong letter, position
    for index in range(len(correctSeq)):
        if not correctSeq[index] == wrongSeq[index]:
            tempArray.append(correctSeq[index])
            tempArray.append(wrongSeq[index])
            tempArray.append(startPos+count)
        count += 1
    return tempArray
