#import regex
import re
import string

emoj_pattern = re.compile(u'([\U00002600-\U000027BF])|([\U0001f300-\U0001f64F])|([\U0001f680-\U0001f6FF])')

#start process_tweet
def processTweet(tweet):
    #Convert to lower case
    tweet = tweet.lower()
    #Remove hyperlinks
    tweet = re.sub(r'https?:\/\/.*\/[a-zA-Z0-9]*', '', tweet)
    #Remove quotes
    tweet = re.sub(r'&amp;quot;|&amp;amp', '', tweet)
    #Remove citations
    tweet = re.sub(r'@[a-zA-Z0-9]*', '', tweet)
    #Remove tickers
    tweet = re.sub(r'\$[a-zA-Z0-9]*', '', tweet)
    #Remove numbers
    tweet = re.sub(r'[0-9]*','',tweet)
    #Remove Punctuation
    exclude = set(string.punctuation)
    tweet = ''.join(ch for ch in tweet if ch not in exclude)
    #Replace #word with word
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
    #Remove emoji
    tweet = emoj_pattern.sub('', tweet)
    #trim
    tweet = tweet.strip('\'"')
    return tweet
#end

#Read the tweets one by one and process it
fp = open('rawData.txt', 'r')
fw = open('PreprocessedData1.txt', 'w')
line = fp.readline()

while line:
    line = line.strip()	
    if line:
    	processedTweet = processTweet(line)
    	print processedTweet
	fw.write(processedTweet+"\n")
    line = fp.readline()
#end loop
fp.close()
fw.close()
