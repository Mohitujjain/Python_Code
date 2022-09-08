#Pickle:
#-->The pickle module implements a fundamental,but powerful algorithm for serializing and de-
# serializing a python object structure.
# Storing data with pickle:-
#-> Booleans,
#-> Integers,
#-> Floats,
#-> Complex Numbers,
#-> (normal and unicode) Strings,
#-> Tuples,
#->  List
#-> Sets, and
#->  Dictionary.

#Pickling Files:
# To use pickle,start by importing it in python. #import pickle
#->Pickle has two main methods.The first one is dump,which dumps an object to a file object and
# the second one is load, which loads an object from a file object.

#Python pickle functions:
#-->1 . dump()-This function is called to serialize an object if hierarchy.
#-->2 . load()-This function is called to de-serialize a data stream.

#Pickling with dump():
#Pickling data is done via the dump() function.It accepts data and a file objects.
#The dump() function then serializes the data and writes it to the file.The syntax of dump() is
# as follows:
# syntax:dump(obj,file)

# import pickle
# ex = {1:"4",2:"3",3:"d"}

# pickle_write = open("text.txt","wb")
# pickle.dump(example, pickle_write)
# pickle_write.close()

#argument-->obj , file
#description-->file object where pickled data will be written


import pickle

list=[10,20,30,40,50,60,87,90]

file=open("datafile.txt","wb")


pickle.dump(list,file)

file.close()