from nltk.corpus import wordnet as wn

graveyard = wn.synset('graveyard.n.01')
cemetery= wn.synset('cemetery.n.01')

print(graveyard.wup_similarity(cemetery))
