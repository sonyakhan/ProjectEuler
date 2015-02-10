def isLargestPalindrome():
	
	highestNum = -1;

	for x in xrange (1000):
		for y in xrange (1000):
			product = x*y
			if isPalindrome(product):
				if product > highestNum:
					highestNum = product				
	return highestNum

def isPalindrome(product):
	palindromeString = str(product)
	for x in xrange (len(palindromeString)):
		
		#print "x = " + str(x)
		#print palindromeString[x]

		if palindromeString[x] != palindromeString[-x-1]:
			#print palindromeString[x] + " " + palindromeString[-x-1]
			return False
	
	return True	




#print isLargestPalindrome()				
print isLargestPalindrome()				