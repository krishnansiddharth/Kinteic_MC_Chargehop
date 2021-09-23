def Next_greater(a,  x):    
	n = len(a) 
	low, high, ans = 0, n - 1,x 
# Continue until low is less
# than or equals to high
	key = (low+high)//2
	while (low <= high):
# Find mid
	mid = (low + high) // 2
        # If element at mid is less than
        # or equals to searching element
		if (a[mid] <= ans):
		    # If mid is equals
		    # to searching element
			if (a[mid] == ans):
				key = mid+1 
			
	 
		    # Make low as mid + 1
			low = mid + 1
	 
		# Make high as mid - 1
		else:
			key  = mid
			high = mid - 1
 
    # Return the next greater element
	return  key

