from nltk import PorterStemmer
# Open File
foutput = open("PreprocessedData1.txt","a")

# Data Stemming
with open('PreprocessedData2.txt', 'r') as f:
        for line in f:
            print line
            singles = []
            stemmer = PorterStemmer()
            for plural in line.split():
		try:
                	singles.append(stemmer.stem(plural))
		except:
			continue
            string = ' '.join(singles)
	    print string
	    foutput.write(string+"\n")	

# Close File
foutput.close()
