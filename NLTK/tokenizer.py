from nltk.tokenize import sent_tokenize,word_tokenize


#here we use sentence tokenizer. What it does is split up the sentence in tokens
#essentially into elements in aa python list. Note that the sentence below has
#two distinct sentences. A general feeeling would be to break sentences using
#punctuations, that being the case the sentence below should be tokenized into
#three tokens noting the full stop after Mr. However, NLTK is a powerful tool
#that considers the difference.
example_text= "Hello Mr. Mehta, how are you? This is great."

#Output sentence tokens as a python list 
print(sent_tokenize(example_text))

#Output word tokens as a python list
print(word_tokenize(example_text))
