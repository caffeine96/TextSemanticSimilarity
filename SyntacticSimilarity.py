	
def lcs(X, Y, m, n):

	if m == 0 or n == 0:
		return 0;
	elif X[m-1] == Y[n-1]:
		return 1 + lcs(X, Y, m-1, n-1);
	else:
		return max(lcs(X, Y, m, n-1), lcs(X, Y, m-1, n));

def nclcs1(a,b):

	j=0;
	# if(b.size()>a.size()):
	# 	swap(a,b);
	if len(b)<len(a):
		a,b = b,a

	ans=0;
	for i in range(0,len(a)):
		
		if a[i] == b[i] :
			ans+=1
			j+=1
		else:
			break;

	#cout<<ans<<endl;
	return ans;

def nclcsn(a,b):

	# if(a.size()>b.size()):
	# 	swap(a,b);
	if len(a)>len(b):
		a,b = b,a

	max1=0;
	ans1=0;
	poss=0;

	for i in range(0,len(a)): # 0 to len(a)-1
		poss=i;

		for j in range(0,len(b)):

			if(a[poss]==b[j]):
				ans1+=1
				poss+=1
				if(poss>=len(a)):
					break

			else:
				if(ans1>0):
					max1=max(max1,ans1)
					ans1=0
					poss=i

		max1=max(max1,ans1)
		ans1=0
		#cout<<max1<<endl;
#	cout<<max1<<endl;
	return max1;

def norm(a,b,c):
	q=float(a*a);
	w1=float(len(b))
	w2=float(len(c))
	q=q/(w1*w2);
	return q;

def final(a,b):
	wght1=0.33;
	wght2=0.33;
	wght3=0.33;
	sum=norm(lcs(a,b,len(a),len(b)),a,b)*wght1+norm(nclcs1(a,b),a,b)*wght2+norm(nclcsn(a,b),a,b)*wght3;
	return sum

#ifstream cin("testcase.txt");
#cin.tie(0);
#cout.tie(0);	
#string a,b;
#cin>>a>>b;
def SyntacticSimilarity(w1,w2):	
	return final(w1,w2)
