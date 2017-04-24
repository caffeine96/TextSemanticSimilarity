from nltk.corpus import state_union,stopwords
from nltk.stem import WordNetLemmatizer,PorterStemmer
from nltk.tokenize import RegexpTokenizer
import collections
import math

#Unique List Function
def unique_list(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x


#Type frequency Function
def type_frequency(w,corp):
	cnt=0
	for i in corp:
		if w==i:
			cnt=cnt+1
	return cnt

#Calculating PMI
#def bigrampmi(tfw,tf,tw,m)
	

def normalized_similarity(similarity,lmbda):
	if similarity>lmbda:
		lmbda=math.ceil(similarity)
	similarity/=lmbda
	return similarity,lmbda


print("Hang on a second!")

train_text=""
#Code for a bigger training set
#fileids=state_union.fileids()
#for i in fileids:
#		train_text+= state_union.raw(i)
#

train_text+= state_union.raw("2006-GWBush.txt")
train_text+= state_union.raw("2000-Clinton.txt")
train_text+= state_union.raw("1981-Reagan.txt")
train_text+= state_union.raw("1971-Nixon.txt")
train_text+= state_union.raw("2004-GWBush.txt")
train_text+= state_union.raw("1947-Truman.txt")
train_text+= state_union.raw("1996-Clinton.txt")
train_text+= state_union.raw("1965-Johnson-1.txt")
train_text+= state_union.raw("1965-Johnson-2.txt")
train_text+= state_union.raw("1975-Ford.txt")


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

m=len(filtered_text)
print("Corpus Words: ",m)
#Getting the unique words(types)
unique= unique_list(filtered_text)
print("Unique Words(Types): ",len(unique))

a=2

#Dictionary for frequency of words
typefr={}
for w in unique:
	typefr[w]=type_frequency(w,filtered_text)

#print(typefr)

w1="nation"
w2="country"

print("Frequency of w1: ",typefr[w1])
print("Frequency of w2: ",typefr[w2])
#print(typefr[w3])
#print(typefr[w4])

neighboursw1=collections.Counter()
n2w1=[]
for i in range(len(filtered_text)):
	if w1==filtered_text[i]:
		neighboursw1[filtered_text[i]]+=1
		for j in range(0,a+1):
			neighboursw1[filtered_text[i+j]]+=1
			neighboursw1[filtered_text[i-j]]+=1

#print(neighboursw1)
pmiw1={}
for t in neighboursw1.keys():
	pmiw1[t]= math.log(neighboursw1[t]*m/(typefr[t]*typefr[w1]),2)

#print(pmiw1) 

neighboursw2=collections.Counter()
n2w2=[]
for i in range(len(filtered_text)):
	if w2==filtered_text[i]:
		neighboursw2[filtered_text[i]]+=1
		for j in range(0,a+1):
			neighboursw2[filtered_text[i+j]]+=1
			neighboursw2[filtered_text[i-j]]+=1

pmiw2={}
for t in neighboursw2.keys():
	pmiw2[t]=math.log((neighboursw2[t]*m/(typefr[t]*typefr[w2])),2)

pmiw1_sorted = sorted(pmiw1, key=pmiw1.get, reverse=True)
pmiw2_sorted = sorted(pmiw2, key=pmiw2.get, reverse=True)
#print(pmiw1_sorted)
#print(pmiw2_sorted)

#Checking common words
#for i in pmiw1_sorted:
#	for j in pmiw2_sorted:
#		if i==j:
#			print(i)

delta=0.7
gamma =3 
b1= math.floor((math.pow(math.log10(typefr[w1]),2)* math.log(len(unique),2))/delta)
b2= math.floor((math.pow(math.log10(typefr[w2]),2) * math.log(len(unique),2))/delta)

print("Beta1: ",b1)
print("Beta2: ",b2)

betasumw1=0
betasumw2=0
for i in range(0,b1+1):
	for j in range(0,b2+1):
		if pmiw1_sorted[i]==pmiw2_sorted[j]:
			betasumw1+=math.pow(pmiw2[pmiw1_sorted[i]],gamma)
			betasumw2+=math.pow(pmiw1[pmiw1_sorted[i]],gamma)		

similarity= betasumw1/b1 + betasumw2/b2
target=open("Lambda.txt","r")
lmbda=float(target.read())
target.close()

similarity,lmbda= normalized_similarity(similarity,lmbda)

target=open("Lambda.txt","w")
target.write(str(lmbda))
target.close()
print("Similarity: 	", similarity)
