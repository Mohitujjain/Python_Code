import pickle

file=open("datafile.txt","rb")

l=pickle.load(file)

print(l)