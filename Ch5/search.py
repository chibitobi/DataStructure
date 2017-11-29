import pdb

def seqSearch(inputlist, item):
	pos = 0
	found = False
	while pos < len(inputlist) and not found:
		if inputlist[pos] == item:
			found = True
		else:
			pos = pos+1

	return found

testlist = [1,2,3,5,5]
print(seqSearch(testlist, 5))


def binSearch(inputlist, item):
	print(inputlist)
	found = False
	pos = len(inputlist)//2
	#pdb.set_trace()
	print("comparing", inputlist[pos], item)
	if (inputlist[pos] is item):
		print("I'm here")
		found = True
	elif (inputlist[pos] < item):
		print("Yeah")
		return binSearch(inputlist[pos:], item)
	
	return found		

print(binSearch(testlist, 4))
