#Name			: RUPANTA RWITEEJ DUTTA
#Date of Creation	: 12.12.2015

#This Program creates a input file named "Input.txt" to be used as an input in the Assignment3.py program.
import random

#Function to genrate input file to be read
fo = open ('Input.txt','w')				# Create and Open File "Input.txt" in Write Mode
fo.write('30')						# Write '30' in the First Line, Indicating the Number of Pages the Process Refers

for num in range (1,10001):				# Generate 10000 Numbers in the Range 1-30
	var = random.randint(1,30)			# Write Each Number on a Different Line
	var = '\n' + str(var)	
	fo.write(var)

fo.close()						# Close File
