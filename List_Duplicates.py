#Checking duplicates in the list by checking each element with its next element
#Works only with sorted lists
def checkDuplications( num ):
    num = num.sort()
    for a,b in zip(num,num[1:]):
        if a == b:
            return False
    return True
    
#Check length of list vs length of its set
def checkDuplications( num ):
    if len(num) == len(set(num)):
        return True
    return False
