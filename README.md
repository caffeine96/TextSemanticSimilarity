## Idea

The idea of the project is to devsing a metric for measuring semantic similarity between words, sentences and ultimately documents. There are many approaches to this NLP problem- finding out word frequency matrix and applying SVM, reducing the dimensions and finally applying Latent Semantic Analysis to find cosines of row vectors hence measuring the similarity. Our approach is of a corpus-based modeling technique that uses Second Order Co-occurence Pointwise Mutual Information along side certain syntactic similarity measures to measure the overall semantic similarity between two sentences.

## Implementation

Consider two sentences: 
```python
s1="The world knows it has lost a heroic champion of justice and freedom"
s2="The earth recognizes the loss of a valliant champoin of independence and justice"
```

We tokenize, lemmatize and remove stopwords, which gives us a refined list of words:
```python
from Cleaner import clean

#Removing punctuations, stopwords and storing important words in a list
sent1=clean(s1)
sent2=clean(s2)
```
![Output](https://github.com/caffeine96/TextSemanticSimilarity/blob/master/TSS%20Snips/Cleaning.png)

[Cleaner Code](https://github.com/caffeine96/TextSemanticSimilarity/blob/master/Cleaner.py)


Length of both the lists are maintained:
```python 
m=len(sent1)
n=len(sent2)
```

Common words in both the lists are identified and extracted. These common words are then subtracted from the original lists. Now, the syntactic and semantic similarlity tests measurement methods are operated on the remaing lists given below as *s1* and *s2*. Go on the link below for the Commonwords code:
```python
from Auxiliary import Commonwords, DisplayMatrixform
#Getting the list of common words and the removal of those words from the original list
common,s1,s2=Commonwords(sent1,sent2)
```

[Commonwords Code](https://github.com/caffeine96/TextSemanticSimilarity/blob/master/Auxiliary.py)

