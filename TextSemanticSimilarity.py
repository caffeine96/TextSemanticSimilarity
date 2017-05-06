from SOCPMI import SemanticSimilarity
from Cleaner import clean
from Auxiliary import Commonwords, DisplayMatrixform
from SimilarityCount import SimilarityCount

s1="The world knows it has lost a heroic champion of justice and freedom"
s2="The earth recognizes the loss of a valliant champoin of independence and justice"

#Removing punctuations, stopwords and storing important words in a list
sent1=clean(s1)
sent2=clean(s2)
m=len(sent1)
n=len(sent2)
#Getting the list of common words and the removal of those words from the original list
common,s1,s2=Commonwords(sent1,sent2)

primat={}
a=2; 
delta=0.7	#Constant depends on the size of the training corpus
gamma =3 	#Defines the weight given to semantic measure. Should be greater than 1.
if len(s2)<len(s1):
	for i in s2:
		primat[i]={}
		for j in s1:
			primat[i][j]=SemanticSimilarity(i,j,a,delta,gamma)
else:
	for i in s1:
		primat[i]={}
		for j in s2:
			primat[i][j]=SemanticSimilarity(i,j,a,delta,gamma)

DisplayMatrixform(primat,s1,s2)

out1=[]
out2=[]
rhosum= SimilarityCount(primat,s1,s2,out1,out2)

print(rhosum)

sentencesimilarity= (len(common)+rhosum)*(m+n)/(2*m*n)
print(sentencesimilarity)
"""
#Semantic Similarity
a=2; 
w1="good"
w2="bad" 
#Returns semantic similarity measure by SOCPMI method
similarity= SemanticSimilarity(w1,w2,a,delta,gamma)
"""
