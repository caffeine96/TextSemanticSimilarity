from Auxiliary import unique_list, type_frequency, normalized_similarity
import collections
import math
import pickle

#Calculating PMI
#def bigrampmi(tfw,tf,tw,m)

def SemanticSimilarity(w1,w2,a,delta,gamma):
	pkl_file=open("Corpus-Train.pkl","rb")
	filtered_text= pickle.load(pkl_file)
	pkl_file.close()

	
	pkl_file2=open("Unique.pkl","rb")
	unique= pickle.load(pkl_file2)
	pkl_file2.close()
	

	pkl_file3=open("Type-Frequency.pkl","rb")
	typefr= pickle.load(pkl_file3)
	pkl_file3.close()
	
	m=len(filtered_text)


	#Dictionary for frequency of words
	#typefr={}
	#for w in unique:
	#	typefr[w]=type_frequency(w,filtered_text)
	
	
	#print(typefr)
	if w1 not in unique:
		return 0
	if w2 not in unique:
		return 0
	print("Frequency of w1: ",typefr[w1])
	print("Frequency of w2: ",typefr[w2])
	#print(typefr[w3])
	#print(typefr[w4])

	neighboursw1=collections.Counter()
	n2w1=[]
	for i in range(len(filtered_text)):
		if w1==filtered_text[i]:
			neighboursw1[filtered_text[i]]+=1
			for j in range(0,a+1):
				neighboursw1[filtered_text[i+j]]+=1
				neighboursw1[filtered_text[i-j]]+=1

	#print(neighboursw1)
	pmiw1={}
	for t in neighboursw1.keys():
		pmiw1[t]= math.log(neighboursw1[t]*m/(typefr[t]*typefr[w1]),2)

	#print(pmiw1) 

	neighboursw2=collections.Counter()
	n2w2=[]
	for i in range(len(filtered_text)):
		if w2==filtered_text[i]:
			neighboursw2[filtered_text[i]]+=1
			for j in range(0,a+1):
				neighboursw2[filtered_text[i+j]]+=1
				neighboursw2[filtered_text[i-j]]+=1

	pmiw2={}
	for t in neighboursw2.keys():
		pmiw2[t]=math.log((neighboursw2[t]*m/(typefr[t]*typefr[w2])),2)

	pmiw1_sorted = sorted(pmiw1, key=pmiw1.get, reverse=True)
	pmiw2_sorted = sorted(pmiw2, key=pmiw2.get, reverse=True)
	#print(pmiw1_sorted)
	#print(pmiw2_sorted)

	#Checking common words
	#for i in pmiw1_sorted:
	#	for j in pmiw2_sorted:
	#		if i==j:
	#			print(i)
	b1= math.floor((math.pow(math.log10(typefr[w1]),2)* math.log(len(unique),2))/delta)
	b2= math.floor((math.pow(math.log10(typefr[w2]),2) * math.log(len(unique),2))/delta)
	if b1>len(pmiw1_sorted):
		b1=len(pmiw1_sorted)
	
	if b2>len(pmiw2_sorted):
		b2=len(pmiw2_sorted)

	print("Beta1: ",b1)
	print("Beta2: ",b2)

	betasumw1=0
	betasumw2=0
	for i in range(0,b1):
		for j in range(0,b2):
			if pmiw1_sorted[i]==pmiw2_sorted[j]:
				betasumw1+=math.pow(pmiw2[pmiw1_sorted[i]],gamma)
				betasumw2+=math.pow(pmiw1[pmiw1_sorted[i]],gamma)		

	similarity= betasumw1/b1 + betasumw2/b2
	target=open("Lambda.txt","r")
	lmbda=float(target.read())
	target.close()

	similarity,lmbda= normalized_similarity(similarity,lmbda)

	target=open("Lambda.txt","w")
	target.write(str(lmbda))
	target.close()

	return similarity
