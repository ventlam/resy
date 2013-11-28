from sets import Set
def calJac():
	set1 = Set(["a","b","c"])
	set2 = Set(["a","b","c"])
	jacad(set1,set2)

def jacad(set_1,set_2):
	n = len(set_1.intersection(set_2));
	return  n/float(len(set_1)+len(set_2)-n)
