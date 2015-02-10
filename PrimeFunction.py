import math


def absVal(number):
	if(number<0):
		number = number*(-1)
	return number	



def isPrime(number):

	if (number==0 or number==1 or number==-1):
		return False

		

	y = int(math.pow(absVal(number), 0.5)) # raises number to the power of 1/2 and rounds up

	for x in xrange(2,y):

		if number%x==0:
			return False
	
	return True
			
print isPrime(600851475143)	

#test function

def absValTest():

	if(not isPrime(100)==False):
		print "This test failed 1"	
		return False
	if(not isPrime(7)==True):
		print "This test failed 2"
		return False	
	if(not isPrime(1)==False):
		print "This test failed 3" 
		return False		
	if(not isPrime(0)==False):
		print "This test failed 4"
		return False	
	if(not isPrime(-500)==False):
		print "This test failed 5"
		return False
	if(not isPrime(-7)==True):
		print "This test failed 6"
		return False
	if(not isPrime(-1)==False):
		print "This test failed 7"
		return False
	
	print "All tests have passed"	

print absValTest()						
	







