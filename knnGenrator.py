from numpy import *
import operator

def createDataSet():
	group = array([[1.0,1.1],[0.8,0.8],[0,0],[0,0.1]])
	label = ['A','A','B','B']
	print group
	return group, label