# 1, Given a list of n numbers, determine if it contains any duplicates
#  n =  [ 2, 4, 3, 5, 7, 7, 9, 9 ]
# make a set and compare set with length with original list  

def has_duplicates(array):
	set1 = set(array)

	if len(set1) == len(array):
		return False
	return True


# to return duplicates  
def what_duplicates(array):
    set1 = set() #make an empty set
    duplicate_list = []
    for item in array:
        if item not in set1:
            set1.add(item) #add to set
        else:
            duplicate_list.append(item)
    return duplicate_list


n =  [ 2, 4, 3, 5, 7, 7, 9, 9 ]
print(has_duplicates(n))
print(what_duplicates(n))