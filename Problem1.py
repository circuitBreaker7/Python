#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
#The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.


#maxV=1000
#y = [3,5]
#stepV = 1
#total = 0
	
#while (stepV < maxV):
#	if (not (stepV % y[0]) or not (stepV % y[1])):
#		total += stepV		
#	stepV += 1
#print("This is the total, ", total)


#For me, the above solution was the obvious solution, but did not seem to be the most efficient or elegant. 
#My thought for the below solution was to reduce the number of times through the loop and the total number of operations
maxV=1000
y = [3,5]
total = 0
stepV = 1
max2 = maxV/y[0]

while(stepV < max2):
	total += stepV * y[0]
	if (stepV % y[0]) and ((stepV * y[1]) < maxV):
		total += stepV * y[1]
	stepV +=1

	
print("The sum of all the multiples of 3 or 5 below 1000 is ", total)