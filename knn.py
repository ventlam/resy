def classify0(inX, dataSet, labels, k):
	dataSetSize = dataSet.shape[0]
	#construct an array by repeating inX by n =(dataSetSize,1) times 
	#a = np.array([0, 1, 2])
	np.tile(a, (2, 2))
	#array([[0, 1, 2, 0, 1, 2],
    # [0, 1, 2, 0, 1, 2]])
	#distance computation
	diffMat = tile(inX , (dataSetSize,1)) - dataSetSize
	sqDiffMat = diffMat**2
	sqDis = sqDiffMat.sum(axis=1)
	dis = sqDis**0.5
	sortDis =dis.argsort()
	classCount={}
	for i in range(k)
		voterlabel = labels[sortDis[i]]
		classCount[voterlabel] = classCount.get(voterlabel,0) + 1
	sortDis = sorted(classCount.itertimes(),key = opeator.itemgetter,reverse =True)
	return sortDis[0][0]


