# microsatellite locator
# not 100% match, with errors
# since every 3 bp creates an amino acid, the error accounts for:
    # if in the error group, only two bp are in the same position as the
    # other groups. Note that the bp must be in the SAME POSITION, not
    # just present. ex) ACAACG is accounted for, ACACAG is not

def U3L6Error(sequence):
	# returns a dictionary of position and sequence
	# checks only for sequences in multiples of 3, length of 6
	count = 1
	dictionary = {}
	nucleotide = ""
	firsthalf = ""
	secondhalf = ""
	for letter in sequence:
		if len(nucleotide) < 5:
                        nucleotide = nucleotide + letter
                        count += 1
                        continue
		else:
                        nucleotide = nucleotide + letter
                        firsthalf = nucleotide[:len(nucleotide)/2]
                        secondhalf = nucleotide[len(nucleotide)/2:]
                        if (not firsthalf == "---") and count % 3 == 0 and checkError(firsthalf, secondhalf):
                                dictionary[count - 6] = str(nucleotide)
                        nucleotide = nucleotide[1:]
                        count += 1
	return dictionary

# parameter is the entire nucleotide of one gene in one species
def U3L9Error(sequence):
	# returns a dictionary of position and sequence
	# checks only for sequences in multiples of 3, length of 9
	count = 1
	dictionary = {}
	array = []
	nucleotide = ""
	firstthird = ""
	secondthird = ""
	thirdthird = ""
	for letter in sequence:
		if len(nucleotide) < 8:
                        nucleotide = nucleotide + letter
                        count += 1
                        continue
		else:
                        nucleotide = nucleotide + letter
                        firstthird = nucleotide[:len(nucleotide)/3]
		        secondthird = nucleotide[len(nucleotide)/3:6]
		        thirdthird = nucleotide[6:]
		        array.append(firstthird)
		        array.append(secondthird)
		        array.append(thirdthird)
                        if (not firstthird == "---") and count % 3 == 0 and checkMicrosatellite(array):
                                dictionary[count - 9] = str(nucleotide)
                        nucleotide = nucleotide[1:]
                        array = []
                        count += 1
	return dictionary

# parameter is the entire nucleotide of one gene in one species
def U3L12Error(sequence):
	# returns a dictionary of position and sequence
	# checks only for sequences in multiples of 3, length of 12
	count = 1
	dictionary = {}
	array = []
	nucleotide = ""
	firstthird = ""
	secondthird = ""
	thirdthird = ""
	fourththird = ""
	for letter in sequence:
		if len(nucleotide) < 11:
                        nucleotide = nucleotide + letter
                        count += 1
                        continue
		else:
                        nucleotide = nucleotide + letter
                        firstthird = nucleotide[:3]
		        secondthird = nucleotide[3:6]
		        thirdthird = nucleotide[6:9]
		        fourththird = nucleotide[9:12]
		        array.append(firstthird)
		        array.append(secondthird)
		        array.append(thirdthird)
		        array.append(fourththird)
                        if (not firstthird == "---") and count % 3 == 0 and checkMicrosatellite(array):
                                dictionary[count - 12] = str(nucleotide)
                        nucleotide = nucleotide[1:]
                        array = []
                        count += 1
	return dictionary

def checkMicrosatellite(array):
        # checks if sequence is a microsatellite
        if len(array) == 4: #U3L12
                if (array[0] == array[1] and array[0] == array[2] and checkError(array[0],array[3])):
                        return True
                elif (array[0] == array[1] and array[0] == array[3] and checkError(array[0],array[2])):
                        return True
                elif (array[0] == array[2] and array[0] == array[3] and checkError(array[0],array[1])):
                        return True
                elif (array[1] == array[2] and array[1] == array[3] and checkError(array[1],array[0])):
                        return True
                else:
                        return False
        elif len(array) == 3: #U3L9
                if (array[0] == array[1] and checkError(array[0],array[2])):
                        return True
                elif (array[0] == array[2] and checkError(array[0],array[1])):
                        return True
                elif (array[1] == array[2] and checkError(array[1],array[0])):
                        return True
                else:
                        return False

def checkError(first, second):
        # ensures at least 67% of bp are in the correct position
        count2 = 0
        for i in range(len(first)):
            if first[i] == second[i]:
                count2 += 1
        if count2 >= 2:
            return True
        else:
            return False

# parameter is the nucleotide file location
def locateWithError(f):
        import collections
        file = open(f, "r")
        array = []
        content = ""
        dic = {}
        dic2 = {}
        dic3 = {}
        for line in file:
                if line[0] == ">":
                        if len(content) > 0:
                                content = content.replace("\n","")
                                dic = U3L9Error(content)
                                dic2 = U3L12Error(content)
                                dic = collections.OrderedDict(sorted(dic.items()))
                                dic2 = collections.OrderedDict(sorted(dic2.items()))
                                dic3[species+"U3L9Error"] = dic
                                dic3[species+"U3L12Error"] = dic2
                                dic3 = collections.OrderedDict(sorted(dic3.items()))
                                array.append(dic3)
                                dic = {}
                                dic2 = {}
                                dic3 = {}
                        if len(line) > 1:
                                species = getSpecies(line[1:])   #####
                        content = ""
                        continue
                else:
                        content += line
        array.sort() # alphabetize
        return array


def getSpecies(line):
    species = ""
    for letter in line:
        if letter == "_":
            break
        else:
            species += letter
    return species

        
