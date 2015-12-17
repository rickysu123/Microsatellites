# checks if proteins created are the same
# parameter is the array output from function proteinLocate
def checkProtein(tempArray):
        if len(tempArray) == 3: #U3L9
                if tempArray[0] == tempArray[1] and tempArray[0] == tempArray[2]:
                        return True
                else:
                        return False
        elif len(tempArray) == 4: #U3L12
                if tempArray[0] == tempArray[1] and tempArray[0] == tempArray[2] and tempArray[0] == tempArray[3]:
                        return True
                else:
                        return False

# parameter is the array output from function locateWithError
# deletes elements in dictionaries that do not create same protein
def refineArray(tempArray, proteinFileLoc):
        for index, dict3 in enumerate(tempArray):
                for entry in dict3.keys(): # U3L9 and U3L12
                        speciesName = entry[:1]
                        length = int(entry[-6])
                        if length == 9:
                                length = 3
                        else:
                                length = 4
                        for position in dict3.get(entry):
                                proteins = proteinLocate(speciesName, position, length, proteinFileLoc)
                                if checkProtein(proteins) == False:
                                        del tempArray[index].get(entry)[position]
        return tempArray
