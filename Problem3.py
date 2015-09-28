#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?
import math
#X=13195

#Brute Force, find all primes, as always
#primeF = [];
#y = 0
#temp = 2
#flag = 0
#while (y < (math.sqrt(X))):
#	if (y % 2): 
#		if not (X % y):
#			while (temp < y/2):
#				if not (y % temp):
#					flag = 1
#					break
#				temp += 1
#			if not flag:
#				primeF.append(y)
#			sum = 0
#			temp = 2
#	y += 1
#print(primeF)


# Hey, but we really only care about the largest!
X = 600851475143
y = (math.sqrt(X))//1
temp, flag = 2, 0
while (y > 1):
	if (y % 2): #Not Even, easy to cut out some iterations
		if not (X % y): 
			while (temp < y/2):
				if not (y % temp):
					flag = 1
					break
				temp += 1		
			if not flag:
				print(y)
				break
	temp, flag = 2, 0
	y -= 1
if y == 1: 
	print("No prime facors, ", X, " is a prime")