################
## The Problem Statement
##
## The nth term of the sequence of triangle numbers is given by, 
## tn = ½n(n+1); so the first ten triangle numbers are:
## 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
## By converting each letter in a word to a number corresponding to 
## its alphabetical position and adding these values we form a word value. 
## For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. 
## If the word value is a triangle number then we shall call the word a triangle word.
## Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing 
## nearly two-thousand common English words, how many are triangle words?
################
## Valerie's Solution
##
## Basically rewrite tn equation: 0 = n^2 + n - 2*tn
## If we have a word, we know what tn is, so we need to solve for
## the n. If there is a solution where n is a positive, whole number
## then we know that tn is a triangle number. 
## I modified the quadractic equation solution to solve the following:
## 		[-1 + sqrt(1 + 8*tn)]/2
## I use X/1 == X//1 to test if X is a whole number, because that was
## the easiest way I knew how to test.
################

import math
file = open('p042_words.txt', 'r') 
words = file.read().split(',')
file.close()

triangle = 0

for wstep in range(0, len(words)):
	words[wstep] = words[wstep].replace('"', '')
	sum = 0
	#Sum the letters
	for step in range(0, len(words[wstep])):
		sum += ((ord(words[wstep][step]) - 64))
		step +=1
	#Check if sum is a triangle number
	p1 = 1 + 8*sum
	if ((math.sqrt(p1)/1) == (math.sqrt(p1)//1)):
		p1 = (-1 + p1)
		if ((p1//2) == (p1/2)):
			triangle += 1
			
print("In this file,", triangle, "of the", len(words), "words were triangle words")