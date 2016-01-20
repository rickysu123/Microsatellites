# microsatellite locator

def U3L6(sequence):
	# returns a dictionary of sequence and position
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
                        if (not firsthalf == "---") and firsthalf == secondhalf and count % 3 == 0:
                                dictionary[count - 6] = str(nucleotide)
                        nucleotide = nucleotide[1:]
                        count += 1
	return dictionary          


def U3L9(sequence):
	# returns a dictionary of sequence and position
	# checks only for sequences in multiples of 3, length of 9
	count = 1
	dictionary = {}
	nucleotide = ""
	firstthird = ""
	secondthird = ""
	thirdthird = ""
	for letter in sequence:
		if len(nucleotide) < 8:
	            nucleotide = nucleotide + letter
	            count = count + 1
		    continue
		else:
			nucleotide = nucleotide + letter
		        firstthird = nucleotide[:len(nucleotide)/3]
		        secondthird = nucleotide[len(nucleotide)/3:6]
		        thirdthird = nucleotide[6:]
		        if (not firstthird == "---") and firstthird == secondthird and firstthird == thirdthird and count % 3 == 0:
				dictionary[count-9] = str(nucleotide)
			nucleotide = nucleotide[1:]
			count = count + 1
	return dictionary


# 4 groups of unit length 3
def U4L12(sequence):
	# returns a dictionary of sequence and position
	# checks only for sequences in multiples of 3, length of 9
	count = 1
	dictionary = {}
	nucleotide = ""
	firstthird = ""
	secondthird = ""
	thirdthird = ""
	for letter in sequence:
		if len(nucleotide) < 11:
                        nucleotide = nucleotide + letter
                        count = count + 1
                        continue
		else:
                        nucleotide = nucleotide + letter
                        firstthird = nucleotide[:len(nucleotide)/3]
                        secondthird = nucleotide[len(nucleotide)/3:8]
                        thirdthird = nucleotide[8:len(nucleotide)]
                        if (not firstthird == "----") and firstthird == secondthird and firstthird == thirdthird and count % 3 == 0:
                                dictionary[count-12] = str(nucleotide)
                        nucleotide = nucleotide[1:]
                        count = count + 1
	return dictionary 

# organize into array
# and array of dictionaries of dictionary
# dic == the output dictionary from method U3L6
# dic2 == the output dictionary from method U3L9
# dic3 == {["rapU3L6", dic], ["rapU3L9", dic2]}
# array == [dic3,dic3,dic3,dic3] (corresponding to [rap, ellus, nvit, muni])
# f is the location of the file
# example
# f = "/Users/rickysu/Desktop/Summer2015Research/MicrosatelliteProject
#         /multi-spec.align.fasta/augustus__SCAFFOLD2__SIZE1116217__proce
#         ssed__gene__0__13__mRNA__1-multi-spec.align.fasta"
# returns an array of a dictionary of 2 dictionaries(U3L6 and U3L9)
def locate(f):
        import collections
        file = open(f, "r")
        arrow = -2
        array2 = ["rap","ellus","nvit", "muni"]
        array = []
        content = ""
        dic = {}
        dic2 = {}
        dic3 = {}
        for line in file:
                if line[0] == ">":
                        arrow += 1
                        if len(content) > 0:
                                content = content.replace("\n","")
                                dic = U3L6(content)
                                dic2 = U3L9(content)
                                dic = collections.OrderedDict(sorted(dic.items()))
                                dic2 = collections.OrderedDict(sorted(dic2.items()))
                                dic3[str(array2[arrow]+"U3L6")] = dic
                                dic3[str(array2[arrow]+"U3L9")] = dic2
                                array.append(dic3)
                                dic = {}
                                dic2 = {}
                                dic3 = {}
                        content = ""
                        continue
                else:
                        content += line
        return array
