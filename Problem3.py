################
## The Problem Statement
##
## The prime factors of 13195 are 5, 7, 13 and 29.
## What is the largest prime factor of the number 600851475143 ?
################
## Brute Force Solution
## This finds all the primes, then you can find the max pretty easily

#X=13195

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

################
## Better Solution
## 
## Realizing we only care about the maximum prime
## we can start at the largest possible number and 
## then step down to the largest prime. 
## We removed some computation by not searching for prime
## of even numbers. We can easily add multiples of 3, 5, etc. 
################

import math
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
				print("The largest prime factor of", X, "is", y)
				break
	temp, flag = 2, 0
	y -= 1
if y == 1: 
	print("No prime facors, ", X, " is a prime")