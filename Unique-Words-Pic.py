from Auxiliary import unique_list
import pickle

pkl_file=open("Corpus-Train.pkl","rb")
filtered_text= pickle.load(pkl_file)
pkl_file.close()
#Getting the unique words(types)
unique= unique_list(filtered_text)

pkl_file2=open("Unique.pkl","wb")
pickle.dump(unique,pkl_file2,-1)
pkl_file2.close()

