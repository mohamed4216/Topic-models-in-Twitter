#!/usr/bin/python
import os
import math

# Number of Docs
doc =  700

# Create Mallet Input file
msg = os.system("mallet-2.0.7/bin/mallet import-dir --input "+str(doc)+"Doc/ --output Mallet2Output/Tweets"+str(doc)+".mallet  --keep-sequence --remove-stopwords") 

# Train LDA model for a range of number of topics and calculate perplexity for each
for Iteration in range(2, 101):

	# Train LDA model
	msg = os.system("mallet-2.0.7/bin/mallet train-topics --num-topics "+ str(Iteration)+" --input Mallet2Output/Tweets"+str(doc)+".mallet --evaluator-filename Mallet2Output/evaluator"+str(doc)+" --num-iterations 100 --random-seed 1")
	
	# Calculate perplexity 
	msg = os.system("mallet-2.0.7/bin/mallet evaluate-topics --evaluator Mallet2Output/evaluator"+str(doc)+" --input Mallet2Output/Tweets"+str(doc)+".mallet --output-doc-probs  Mallet2Output/docprobs"+str(doc)+".txt")
	
	msg = os.system("mallet-2.0.7/bin/mallet run cc.mallet.util.DocumentLengths --input Mallet2Output/Tweets"+str(doc)+".mallet > Mallet2Output/doclengths"+str(doc)+".txt")
	
	logLikelihood=0
	totalWords=0
	docProb = open("Mallet2Output/docprobs"+str(doc)+".txt", "r") 
	docLength = open("Mallet2Output/doclengths"+str(doc)+".txt", "r")	
	Line = docProb.readline()
	while Line :
		logLikelihood = float(Line)
		totalWords = float(docLength.readline())	
		Line = docProb.readline()
	docProb.close()
	docLength.close()
	perplexity = int(math.exp(-1 * logLikelihood/totalWords))
	PerpFile = open("Mallet2Output/perplexity"+str(doc)+".txt", "a")
	PerpFile.write(str(Iteration) + " : " + str(perplexity)+"\n")
	PerpFile.close()

