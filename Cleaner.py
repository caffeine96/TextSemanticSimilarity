from nltk.stem import WordNetLemmatizer,PorterStemmer
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

def clean(s1):
	stat=[]
	stop_words=set(stopwords.words("english"))

	#Tokenizing the sentence
	tokenizer= RegexpTokenizer(r'\w+')
	words=tokenizer.tokenize(s1)

	#Stemmer and Lemmatizer instance created
	ps=PorterStemmer()
	lemmatizer= WordNetLemmatizer()

	#Lemmatizing words and adding to the final array if they are not stopwords
	for w in words:
		if w not in stop_words:
			w=lemmatizer.lemmatize(w)		
			stat.append(w)
	return stat
