def smallestMultiple():


	count = 20

	while (True):
		
		if (count%11==0 and count%12==0 and count%13==0 and count%14==0 and count%15==0 and count%16==0 and count%17==0 and count%18==0 and count%19==0 and count%20==0):
			return count

		else:
			count+=1

print smallestMultiple()

		