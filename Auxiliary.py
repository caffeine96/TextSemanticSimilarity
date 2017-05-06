import math
#Unique List Function
def unique_list(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x

#Type frequency Function
def type_frequency(w,corp):
	cnt=0
	for i in corp:
		if w==i:
			cnt=cnt+1
	return cnt

#Returning Normalized Similarity
def normalized_similarity(similarity,lmbda):
	if similarity>lmbda:
		lmbda=math.ceil(similarity)
	similarity/=lmbda
	return similarity,lmbda


#List of common words from two lists returned
def Commonwords(s1,s2):
	common=list(set(s1).intersection(s2))
	news1=list(set(s1).difference(common))	
	news2=list(set(s2).difference(common))
	return common,news1,news2

def DisplayMatrixform(primat,s1,s2):
	for i in s2:	
		print("\t",i,end=' ')	
	
	for j in s1:
		print("")
		print(j,end=' ')
		for i in s2:	
			print("\t",primat[j][i],end=' ')

	print(" ")
		

