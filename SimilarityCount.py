
def SimilarityCount(primat,s1,s2,out1,out2):
	max=0	
	if len(s1) == len(out1):
		return 0

	for i in s1:
		if i not in out1:
			for j in s2:
				if j not in out2:
					if primat[i][j]>max:
						max=primat[i][j]
						maxi=i
						maxj=j
	
	
	if max==0:
		return 0
	else:
		out1.append(maxi)
		out2.append(maxj)

	return max + SimilarityCount(primat,s1,s2,out1,out2)			
