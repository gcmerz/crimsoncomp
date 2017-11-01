def swapchars (original):
	most = original[0]
	least = original[0]
	max = original.count(original[0])
	min = original.count(original[0])

	for c in original:
	    if c is not " ":
	        if original.count(c) > max:
	            most = c
	            max = original.count(c)
	        if original.count(c) < min:
	            least = c
	            min = original.count(c)

	original = original.replace(most, '#')
	original = original.replace(least, '$')
	original = original.replace('#', least)
	original = original.replace('$', most)
	return original