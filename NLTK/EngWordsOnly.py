from nltk.corpus import words,stopwords
from nltk.tokenize import RegexpTokenizer

stop_words=set(stopwords.words("english"))

#Tokenizing the sentence
tokenizer= RegexpTokenizer(r'\w+')
words=tokenizer.tokenize(train_text)
eng_words=words.words()

filtered_text= []

for w in words:
    if w not in stop_words:
		if w in eng_words:
	    	filtered_text.append(w)

print(filtered_text)
