from nltk.corpus import state_union,stopwords
from nltk.stem import WordNetLemmatizer,PorterStemmer
from nltk.tokenize import RegexpTokenizer
import collections
import pickle
from Auxiliary import unique_list

#Calculating PMI
#def bigrampmi(tfw,tf,tw,m)
	
print("Hang on a second!")

train_text=""
#Code for a bigger training set
fileids=state_union.fileids()
for i in fileids:
		train_text+= state_union.raw(i)


#train_text+= state_union.raw("2006-GWBush.txt")
#train_text+= state_union.raw("2000-Clinton.txt")
#train_text+= state_union.raw("1981-Reagan.txt")
#train_text+= state_union.raw("1971-Nixon.txt")
#train_text+= state_union.raw("2004-GWBush.txt")
#train_text+= state_union.raw("1947-Truman.txt")
#train_text+= state_union.raw("1996-Clinton.txt")
#train_text+= state_union.raw("1965-Johnson-1.txt")
#train_text+= state_union.raw("1965-Johnson-2.txt")
#train_text+= state_union.raw("1975-Ford.txt")
#train_text+= state_union.raw("1951-Truman.txt")
#train_text+= state_union.raw("1950-Truman.txt")
#train_text+= state_union.raw("1949-Truman.txt")
#train_text+= state_union.raw("1948-Truman.txt")
#train_text+= state_union.raw("1946-Truman.txt")
#train_text+= state_union.raw("1945-Truman.txt")
#train_text+= state_union.raw("1953-Eisenhower.txt")
#train_text+= state_union.raw("1954-Eisenhower.txt")
#train_text+= state_union.raw("1955-Eisenhower.txt")
#train_text+= state_union.raw("1956-Eisenhower.txt")


stop_words=set(stopwords.words("english"))

#Tokenizing the sentence
tokenizer= RegexpTokenizer(r'\w+')
words=tokenizer.tokenize(train_text)

#Stemmer and Lemmatizer instance created
ps=PorterStemmer()
lemmatizer= WordNetLemmatizer()

#The sequence to get the stop words removed from the sentence
filtered_text= []

#Lemmatizing words and adding to the final array if they are not stopwords
for w in words:
    if w not in stop_words:
	    w=lemmatizer.lemmatize(w)		
	    filtered_text.append(w)
#print(filtered_text)
print("Corpus Words: ",len(filtered_text))

output = open("Corpus-Train.pkl","wb")
pickle.dump(filtered_text,output,-1)
output.close()

