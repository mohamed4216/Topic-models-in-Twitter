##!/usr/bin/python
import os

# Splitting Data 
Docname= 700
msg = os.system("mkdir "+str(Docname)+"Doc/")	
fopen = open("PreprocessedData2.txt", 'r')
count = 0
Line = fopen.readline()
NumberLines = int(23000/Docname)
while Line :
	if(Line.rstrip()):
		quotient = count / NumberLines
		TempFile = open(str(Docname)+"Doc/Tweet"+str(quotient)+".txt", 'a')
		TempFile.write(Line)
		TempFile.close()
		count = count + 1
	Line = fopen.readline()

fopen.close()

