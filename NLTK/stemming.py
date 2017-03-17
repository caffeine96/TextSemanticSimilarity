#Stemming- Used for data pre-processing
#To get the root(stem) of the word

#Consider the following two sentences that are similar in
#meaning-
#I was taking a ride in the car
#I was riding in the car
#Stemming is used to extract the core meaning of the sentence

from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps=PorterStemmer()
example_words=["ride","rider","riding","rided","ridly"]

for w in example_words:
    print(ps.stem(w))

new="It is very important to be ridigly while you are riding with ride. All riders have rided poorly."

words=word_tokenize(new)

for w1 in words:
    print(ps.stem(w1))
