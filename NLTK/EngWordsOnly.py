from nltk.corpus import stopwords
import enchant
from nltk.tokenize import RegexpTokenizer

stop_words=set(stopwords.words("english"))

train_text="My name is maaru naam Maitrey"
#Tokenizing the sentence
tokenizer= RegexpTokenizer(r'\w+')
words=tokenizer.tokenize(train_text)
d = enchant.Dict("en_US")

filtered_text= []


for w in words:
	if w not in stop_words:
		if d.check(w):
			filtered_text.append(w)

print(filtered_text)

