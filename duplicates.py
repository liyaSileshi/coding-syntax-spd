#given a list of n numbers, determine if it contains any duplicates
#  n =  [ 2, 4, 3, 5, 7, 7, 9, 9 ]
# make a set and compare set with length with original list  


def has_duplicates(array):
	s1 = set(array)

	if len(s1) == len(array):
		return False
	return True

# to return duplicates

def what_duplicates(array):
	s1 = set()
	dupes = []
	
for item in array:
		if item not in s1:
			s1.add(item)
		else:
			dupes.append(item)

	return dupes
