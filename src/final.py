# parameters are location of the nucleotide file, 
# and the location of the output textfile
def final(fileLoc, outputLocation):
    import os # this is to get the file name
    separate = "___________________________________________________________________"
    proteinFileLoc = getProteinFile(fileLoc)
    array = locateWithError(fileLoc)
    array = refineArray(array,proteinFileLoc)
    arrayU3L9 = []
    arrayU3L12 = []
    # split array into array9 and array12
    for dict3 in array:
	d9 = dict(dict3.items()[len(dict3)/2:])
	d12 = dict(dict3.items()[:len(dict3)/2])
	arrayU3L9.append(d9)
	arrayU3L12.append(d12)
    # get exact name of gene/file name
    name = os.path.split(fileLoc)[1]
    # get longest dictionary length in array9 and array12
    length9 = getLongestDict(arrayU3L9)
    length12 = getLongestDict(arrayU3L12)
    # create text file with the name of the gene
    textFile = open(str(outputLocation),"a")
    textFile.write(separate+separate+"\n\n")
    textFile.write(name) # write file name
    textFile.write("\n\n")
    # write in file
    if checkEmpty(arrayU3L9):
        textFile.write("No microsatellites of length 9bp.\n\n")
    else:
        textFile.write("Microsatellites of length 9bp.\n\n")
        textFile.write("\t\tPosition\tSequence\tAmino-Acid Sequence\tMicrosatellite Type\n")
        write(textFile, fileLoc, proteinFileLoc, arrayU3L9, length9)
    textFile.write("\n\n")
    if(checkEmpty(arrayU3L12)):
	textFile.write("No microsatellites of length 12bp.\n\n")
    else:
        textFile.write("Microsatellites of length 12bp.\n\n")
        textFile.write("\t\tPosition\tSequence\tAmino-Acid Sequence\tMicrosatellite Type\n\n")
        write(textFile, fileLoc, proteinFileLoc, arrayU3L12, length12)
    textFile.write(separate+separate+"\n\n")
    textFile.close()

def getProteinFile(fileLoc):
    proteinFileLoc = fileLoc
    proteinFileLoc = proteinFileLoc.replace(".fasta","pep.fasta")
    return proteinFileLoc
