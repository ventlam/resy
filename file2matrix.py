def file2matrix(filename):
	fr = open(filename)
	numberofLines = len(fr.readlines())
	returnMat = zeros((numberofLines,3))
	classLabelVetor = []
	fr = open(filename)
	index =0
	for(i in numberofLines)

