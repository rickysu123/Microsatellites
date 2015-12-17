def checkEmpty(array):
        # when the array is separated into array9 and array12,
        # the parameter is either array12 or array9, to check if either is empty
        # returns True if empty
	count = 0
	for dic in array:
		# check if there are any elements in the dictionary in the array
		for key in dic.keys():
			if len(dic.get(key)) > 0:
				count += 1
			if count > 0:
				return False
	else:
		return True

# make a function that takes the two arrays and the file name,
# and writes it in a text file


# split array into array9 and array12
# start with empty arrays!
for dict3 in array:
	d9 = dict(dict3.items()[len(dict3)/2:])
	d12 = dict(dict3.items()[:len(dict3)/2])
	array9.append(d9)
	array12.append(d12)


# get longest dictionary in array9 or array12
# set length to 0 first!
def getLongestDict(array9):
    length = 0
    for dic in array9:
            for key in dic.keys():
                    if length < len(dic.get(key)):
                            length = len(dic.get(key))
    return length


# parameters are the output textFile, location of the nucleotide text file,
# nucArray = array9 or array12,
# and longest length of dictionary in array9 or array12
def write(textFile,nucleoFileLoc,proteinFileLoc,nucArray,length):
        import sys
        for index in range(length):
            textFile.write("\n")
            # find the lowest position within the current dictionaries
            # to compare to other dictionaries
            position = sys.maxint
            for dic in nucArray:
                    tempDic = dic[dic.keys()[0]]
                    if len(tempDic) > 0:
                            if tempDic.keys()[0] < position:
                                    position = tempDic.keys()[0]
                    else:
                            continue
            # find the lowest position within the current dictionaries
            # to compare to other dictionaries
            for index2, dic in enumerate(nucArray):
                    species = "" # keep tack of species
                    length = 0 # keep track of length 9 or 12
                    tempDic = dic[dic.keys()[0]]
                    # write species name
                    if dic.keys()[0][-6] == "9":
                        length = 9
                        species = dic.keys()[0][:-9]
                    else:
                        length = 12
                        species = dic.keys()[0][:-10]
                    textFile.write(species[:7]) # species
                    if len(tempDic) == 0: # ERROR
                    # mostly for U3L12
                    # for if there are no entries in the dictionary 
                        shortWrite(textFile, position, species, length, nucleoFileLoc, proteinFileLoc)
                    else:
                        if not position == tempDic.keys()[0]: # ERROR
                        # if the position is not in a dictionary because the sequence
                        # does not produce a correct amino-acid sequence
                            shortWrite(textFile, position, species, length, nucleoFileLoc, proteinFileLoc)
                        else: # CORRECT
                                textFile.write("\t\t")
                                textFile.write(str(position)) # position
                                textFile.write("\t\t")
                                textFile.write(str(tempDic.get(position))) # sequence
                                textFile.write("\t")
                                protein = proteinLocate(species,position,length/3,proteinFileLoc)
                                textFile.write(str("".join(protein))) # amino-acid sequence
                                textFile.write("\t\t\t")
                                microType = checkMicroType(str(tempDic.get(position)))
                                textFile.write(writeMicroType(microType)) # micro type
                                textFile.write("\n")
                                tempDic2 = nucArray[index2]
                                del tempDic2[tempDic2.keys()[0]][position]
                                nucArray[index2] = tempDic2

# for writing into the text file when one species does not contain the
# microsatellite that the other species contains
def shortWrite(textFile, position, species, length, nucleoFileLoc, proteinFileLoc):
        textFile.write("\t\t")
        textFile.write(str(position))
        textFile.write("\t\t")
        nucLetters = nucleotideLocate(str(species), position, length, nucleoFileLoc)                       
        textFile.write(str("".join(nucLetters)))
        textFile.write("\t")
        proteinLetters = proteinLocate(str(species),position, length/3, proteinFileLoc)
        textFile.write(str("".join(proteinLetters))) # protein sequence
        textFile.write("\t\t\t")
        textFile.write("Not a microsatellite")
        textFile.write("\n")


# for writing into the text file the type of microsatellite
# parameter is the array that contains correct letter, wrong letter, and position
def writeMicroType(microType):
        if len(microType) == 1:
                return microType[0]
        else:
                output = "Interrupted, replacement of '%s' with '%s' at position %d" % (microType[0],microType[1],microType[2])
                return output
