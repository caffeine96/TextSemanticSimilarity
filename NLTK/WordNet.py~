from nltk.corpus import wordnet

#Synonyms for the word program. Stored in a list
syns= wordnet.synsets("program")
print(syns)
print(syns[0].lemmas())
#just the word
print(syns[0].lemmas()[0].name())

#definition
print(syns[0].definition())

#examples
print(syns[0].examples())


#Displaying the list of synonyms and antonyms
synonyms= []
antonyms= []

for syn in wordnet.synsets("good"):
    for l in syn.lemmas():
        synonyms.append(l.name())
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())

print(set(synonyms))
print(set(antonyms))

#Compare similarity between two words
w1= wordnet.synset("ship.n.01")
w2= wordnet.synset("boat.n.01")

#wup is named after scientists discovering semantic similarity
print(w1.wup_similarity(w2))
