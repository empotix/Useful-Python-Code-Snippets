#Insertion Sort

len, ar = int(input()),list(map(int,input().split()))
for i in range(1,len):
    current = ar[i]
    
    for j in range(i-1,-1,-1): 
        if ar[j] > current:                 #If previous number is greater than the current number
            ar[j], ar[i] = ar[i], ar[j]     #Swapping the numbers to get the smaller number to the left    
            i = j                           #Current element is now at a different location
        else:
            break                           #If a number is greater than the number to its left since the array to the left is already sorted
    print(' '.join(list(map(str,ar))))
