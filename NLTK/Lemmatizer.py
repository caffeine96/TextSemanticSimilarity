
from nltk.stem import WordNetLemmatizer
#Lemmatizing is similar to stemming. The output would be a
#some form of a synonym to the input word
#Lemmatizer is better than stemming
lemmatizer= WordNetLemmatizer()

#default is pos is 'n' 
print(lemmatizer.lemmatize("rides",pos="v"))
print(lemmatizer.lemmatize("rode",pos="v"))
print(lemmatizer.lemmatize("ridden",pos="v"))
print(lemmatizer.lemmatize("riding",pos="v"))
print(lemmatizer.lemmatize("better",pos="a"))
