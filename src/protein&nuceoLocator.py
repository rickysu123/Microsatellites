# protein locator
# parameter is the name of species in String form(rap,ellus...) (name),
    # position of the microsatellite (position),
    # the number of proteins wanted (amount),
    # nucelotide file location (f)
# the function will automatically change the location to the protein file


def proteinLocate(speciesName, position, amount, proteinFileLoc):
        speciesName = speciesName[:1] # take first letter only
        array = []
        content = ""
        file = open(proteinFileLoc,"r")
        while True:
            temp = file.readline()
            if temp[:2] == ">" + speciesName:
                break
        while True:
            temp = file.readline()
            if temp[0] == ">":
                break
            content += temp
        content = content.replace("\n","")
        proteinPosition = position/3
        content = content[proteinPosition:]
        letters = []
        for letter in range(amount):
            letters.append(content[letter])
        return letters


# function is to get a nucleotide sequence
# specifically for when a species has a microsatellite at a certain position,
# but another species does not have that microsatellite at that position

def nucleotideLocate(speciesName, position, amount, f):
    tempFile = open(f, "r")
    speciesName = speciesName[:1] # take first letter only
    content = "" # put entire nucleotide sequence in here as a string
    while True:
            temp = tempFile.readline()
            if temp[:2] == ">" + speciesName:
                break
    while True:
            temp = tempFile.readline()
            if temp[0] == ">":
                break
            content += temp
    content = content.replace("\n","")
    content = content[position:]
    letters = []
    for letter in range(amount):
        letters.append(content[letter])
    return letters
