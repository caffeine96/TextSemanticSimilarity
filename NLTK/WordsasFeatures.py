import nltk
import random
from nltk.corpus import movie_reviews

#One Liner
##documents= [(list(movie_reviews.words(fileid)),category)
##            for category in movie_reviews.categories()
##            for fileid in movie_reviews.fileids(category)]

documents=[]

#Movies list and resposne classified as positive and negative
for category in movie_reviews.categories():
    for fileid in movie_reviews.fileids(category):
        documents.append((list(movie_reviews.words(fileid)),category))
        
random.shuffle(documents)

#print(documents[1])
all_words=[]
for w in movie_reviews.words():
    all_words.append(w.lower())

#Frequency Distribution    
all_words=nltk.FreqDist(all_words)
word_features= list(all_words.keys())[:3000]
#print(all_words.most_common(15))
#print(all_words["stupid"])

def find_features(document):
    words= set(document)
    features={}
    for w in word_features:
        features[w]={w in words}
    return features

	
#print((find_features(movie_reviews.words('neg/cv000_29416.txt'))))
featuresets=[(find_features(rev),category) for(rev, category) in documents]
print(featuresets)
