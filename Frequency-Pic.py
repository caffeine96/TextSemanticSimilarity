import pickle
import collections

pkl_file=open("Corpus-Train.pkl","rb")
filtered_text= pickle.load(pkl_file)
pkl_file.close()

typefr=collections.Counter()
for w in filtered_text:
	typefr[w]+=1

pkl_file2=open("Type-Frequency.pkl","wb")
pickle.dump(typefr,pkl_file2,-1)
pkl_file2.close()
