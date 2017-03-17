from nltk.corpus import stopwords
# Stop words are trivial words on which data analysis is useless
# Something like 'A','An','The'
from nltk.tokenize import word_tokenize

example_sentence="My name is Maitrey Mehta. Who are you? This is marvellous"
#There is an inbuilt dictionary of stop words for the English language
stop_words=set(stopwords.words("english"))
#print(stop_words)

#Tokenizing the sentence
words=word_tokenize(example_sentence)

#The sequence to get the stop words removed from the sentence
filtered_sentence= []

for w in words:
    if w not in stop_words:
        filtered_sentence.append(w)

print(filtered_sentence)

#or

filtered_sentence2=[w for w in words if not w in stop_words]
print(filtered_sentence2)
