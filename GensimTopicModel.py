from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
import gensim

tokenizer = RegexpTokenizer(r'\w+')

#create English stop words list
en_stop = get_stop_words('en')
    
#compile sample documents into a list
doc_set = []

for i in range (0,700):
    s="Tweet"+str(i)+".txt"
    a=open('700Doc/'+s,'r')
    b=a.read().decode('utf8', 'ignore')
    c=b.replace("\n", "")
    doc_set.append(c)

# list for tokenized documents in loop
texts = []

# loop through document list
for i in doc_set:
    # clean and tokenize document string
    raw = i.lower()
    tokens = tokenizer.tokenize(raw)
    stopped_tokens = [i for i in tokens if not i in en_stop]  
    texts.append(stopped_tokens)
    
# turn our tokenized documents into a id <-> term dictionary
dictionary = corpora.Dictionary(texts)

# convert tokenized documents into a document-term matrix
corpus = [dictionary.doc2bow(text) for text in texts]

num_topics=20

# Output LDA topic model
ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics, id2word = dictionary, passes=20)
foutput=open('GensimModelOutput.txt','a')
foutput.write(str(ldamodel.print_topics(num_topics, num_words=10)))
foutput.close()


    

