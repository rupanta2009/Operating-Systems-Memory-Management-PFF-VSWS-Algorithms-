# Program		: ASSIGNMENT 3 (PFF & VSWS Algorithms)	
# Name			: RUPANTA RWITEEJ DUTTA
# Email Address		: rrd300@nyu.edu
# Date of Creation	: 12.12.2015
# School		: NYU Tandon School of Engineering
# NYU ID		: N15786532
# Net ID		: rrd300
# Subject		: Introduction to Operating System

# This Program takes a file as input on the command line and calculates number of page faults by implementing the PFF 
#   and VSWS Algorithms.
import sys

# Function to read input file
def readFile(fileName):
	try:
		fo = open(fileName,'r')
	except:
		print "\nERROR: Unable to Open Input File: '%s'\nPlease Check: Path/FileName" %fileName
		print "----------------------------------------------\n"
		exit(0)
	else:	
		data = fo.read()
		attributes = data.split("\n")
		return attributes
		fo.close()

# Function to Implement PFF
#-------------------------------------------------------------------
# Sample Outputs:
# 	Number of Pages the Process Occupies	: 30
#	Total Number of Page References		: 10000
#-------------------------------------------------------------------
# F	Min Frames	Frames < 10	Max Frames	Page Faults
#-------------------------------------------------------------------
# 5	1		87		30		1324
# 10	1		10		30		104
# 15	1		10		30		30
# 20	1		10		30		30
# 25	1		10		30		30
#-------------------------------------------------------------------
# The number of page faults decreases significantly with the
#  increase in the value of 'F' and becomes constant after a certain 
#  value.
#-------------------------------------------------------------------
def pff(attributes):
	pageFaultCount = 0
	fValue = 10
	tValue = 0
	minCount = 10000
	maxCount = 0
	tenCount = 0
	dictionary = {}
	for index in attributes:						# Pick Page from the List of Sequencial Page References
		key = index
		value = 1			
		if index not in dictionary.keys():				# Page Fault Occurs
			pageFaultCount = pageFaultCount + 1			# Increament Page Fault Count
			if tValue >= fValue:					# Page Fault Occurs and T >= F
				for num in dictionary.keys():			# Remove Pages with Use Bit = 0
					if dictionary[num] == 0:
						del dictionary[num]
				for num in dictionary.keys():			# Set Use Bits of Remaining Pages to 0
					dictionary[num] = 0
				dictionary[key] = value				# Add New Page to Set
				tValue = 0
			else:							# Page Fault Occurs and T < F
				dictionary[key] = value				# Add New Page to Set
				tValue = 0
		else:								# Page Found in Memory. No Page Fault Occurs
			dictionary[key] = value					# Add New Page to Set
			tValue = tValue + 1
		if len(dictionary) < minCount:					# Count Minimum Number of Frames Allocated
			minCount = len(dictionary)
		if len(dictionary) < 10:					# Count Number of Times less than 10 Frames are Allocated
			tenCount = tenCount + 1
		if len(dictionary) > maxCount:					# Count Maximum Number of Frames Allocated
			maxCount = len(dictionary)
	print "\n----------------------------------------------"
	print "Result: PFF (Parameters: F %d)" %fValue
	print "----------------------------------------------"
	print "Minimum Number of Frames Allocated : %d" %minCount
	print "Frequency of less than 10 Frames   : %d" %tenCount
	print "Maximum Number of Frames Allocated : %d" %maxCount
	print "Total Number of Page Faults in PFF : %d" %pageFaultCount
	print "----------------------------------------------\n"

# Function to Implement VSWS
#-----------------------------------------------------------------------------------
# Sample Outputs:
# 	Number of Pages the Process Occupies	: 30
#	Total Number of Page References		: 10000
#-----------------------------------------------------------------------------------
# M	L	Q	Min Frames	Frames < 10	Max Frames	Page Faults
#-----------------------------------------------------------------------------------
# 5	15	10	1		25		28		3921
# 10	20	15	1		18		30		369
# 15	25	20	1		15		30		305
# 20	30	25	1		10		30		79
# 25	35	30	1		10		30		39
#-----------------------------------------------------------------------------------
# The number of page faults decreases significantly with the increase in the values
#  of 'M', 'L' and 'Q'.
#-----------------------------------------------------------------------------------
def vsws(attributes):
	pageFaultCount = 0
	pageFaults = 0
	mValue = 20
	lValue = 30
	qValue = 25
	tValue = 0
	minCount = 10000
	maxCount = 0
	tenCount = 0
	dictionary = {}
	for index in attributes:						# Pick Page from the List of Sequencial Page References
		key = index
		value = 1			
		if index not in dictionary.keys():				# Page Fault Occurs
			pageFaultCount = pageFaultCount + 1
			pageFaults = pageFaults + 1
			if tValue >= lValue:					# If T >= L
				for num in dictionary.keys():
					if dictionary[num] == 0:		# Remove Pages with Use Bit = 0
						del dictionary[num]
				for num in dictionary.keys():			# Set Use Bits of Remaining Pages to 0
					dictionary[num] = 0
				dictionary[key] = value				# Add New Page to Set
				tValue = 0
				pageFaults = 0
			else:							# If T < L
				if pageFaults > qValue and tValue >= mValue: 	# If Virtual Time since Last Sampling >= M and pageFaults > Q
					for num in dictionary.keys():		# Remove Pages with Use Bit = 0
						if dictionary[num] == 0:
							del dictionary[num]
					for num in dictionary.keys():		# Set Use Bits of Remaining Pages to 0
						dictionary[num] = 0
					dictionary[key] = value			# Add New Page to Set			
					tValue = tValue + 1
					pageFaults = 0
				else:						# If Virtual Time since Last Sampling < M	
					dictionary[key] = value			# Add New Page to Set
					tValue = tValue + 1
		else:								# Page Found in Memory. No Page Fault Occurs
			dictionary[key] = value					# Add New Page to Set
			tValue = tValue + 1
		if len(dictionary) < minCount:					# Count Minimum Number of Frames Allocated
			minCount = len(dictionary)
		if len(dictionary) < 10:					# Count Number of Times less than 10 Frames are Allocated
			tenCount = tenCount + 1
		if len(dictionary) > maxCount:					# Count Maximum Number of Frames Allocated
			maxCount = len(dictionary)
	print "\n----------------------------------------------"
	print "Result: VSWS (Parameters: M %d, L %d, Q %d)" %(mValue, lValue, qValue)
	print "----------------------------------------------"
	print "Minimum Number of Frames Allocated : %d" %minCount
	print "Frequency of less than 10 Frames   : %d" %tenCount
	print "Maximum Number of Frames Allocated : %d" %maxCount
	print "Total Number of Page Faults in VSWS: %d" %pageFaultCount
	print "----------------------------------------------\n"

# Main Function
def main():
	print "\n\n----------------------------------------------"
	print "Page Replacement Algorithms: PFF & VSWS"
	print "----------------------------------------------"
	fileName = sys.argv[1]
	attributes = readFile(fileName)
	print "Input File Name                     : %s" %fileName
	print "Number of Pages the Process Occupies: %s" %attributes[0]
	print "----------------------------------------------\n"
	attributes.remove(attributes[0])
	pff(attributes)
	vsws(attributes)	

if __name__ == "__main__":
	main()
