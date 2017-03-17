import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer


train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")

custom_sent_tokenizer= PunktSentenceTokenizer(train_text)
tokenized= custom_sent_tokenizer.tokenize(sample_text)

def process_content():
    try:
        for i in tokenized:
            words=nltk.word_tokenize(i)
            tagged=nltk.pos_tag(words)
            #Named Entity are persons,organiztions etc
            #If nltk.ne_chunk(tagged,binary=True) it gives
            #whether a POS is a named entity or not
            namedEnt=nltk.ne_chunk(tagged)
            namedEnt.draw()
    except Exception as e:
        print(str(e))

process_content()


##
##NE Type Examples
##
##ORGANISATION
##PERSON
##LOCATION
##DATE
##TIME
##MONEY
##PERCENT
##FACILITY
##GPE(Geoprahical location)
