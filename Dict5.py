#Dictionary:-
#A dictionary is a collection which is unordered .In python dictionaries are written with
# curly brackets {}.
# A dictionary has a key:value pair.

d={
    'name':'python',
    'fees':'40000',
    'duration':'2months'

}
#print(type(d))   #type
#f=d['fees']      # access value
#print(f)

for n in d:  #iteration
    #print(n)  # only keys return you
    print(d[n]) #only  value return

#Dict function:get(),keys(),values(),items().
#get():returns the value   #d.get('') #n=d['name']
#del(),pop(),update(),clear()-u can change using keys in dict with the help of del and pop func
d={
    'name':'mohit',
    'sal':'1000000',
    'experience':'5yrs'
}

c=d.get('name') #exp1
print(c)
c1=d['name']   #exp2
print(c1)

#keys:
d={
    'name':'mohit',
    'sal':'1000000',
    'experience':'5yrs'
}
for a in d.keys(): # if you want values then u simply change .keys =.values, #for a in d.values()
    print(a)

#items:-
d={
    'name':'mohit',
    'sal':'1000000',
    'experience':'5yrs'
}
for a,b in d.items():
    print(a,b)

#del
d={
    'name':'mohit',
    'sal':'1000000',
    'experience':'5yrs'
}
del d['sal']
print(d)

#pop:
d={
    'name':'mohit',
    'sal':'1000000',
    'experience':'5yrs'
}
print(d.pop('experience')) #pop return the deleted value.
print(d)

#dict:
d=dict(name="bmw",price=20000)
print(d)

#update:
d={
    'name':'mohit',
    'sal':'1000000',
    'experience':'5yrs'
}
d.update({'sal':400000}) #update the value
print(d)

#clear():
d={
    'name':'mohit',
    'sal':'1000000',
    'experience':'5yrs'
}
d.clear() #clear the data
print(d)

#insert :
d={
    'name':'mohit',
    'sal':'1000000',
    'experience':'5yrs'
}
d['desc']='This is Python'  #insert data
print(d)

d={
    'name':'mohit',
    'sal':'1000000',
    'experience':'5yrs'
}
d['fees']='10000'  #insert data
print(d)

#Nested Dictionary:
#->Nested Dict:means putting a dict inside another dict.
#->It's a collection of dict into one single dict.
#Create :
company={
    'bmw':{'emi':'5yrs','downpayment':800000},
    'OD':{'emi':'5yrs','downpayment':850000},
    'merceideze':{'emi':'5yrs','downpayment':850000},
}
print(company)
company['OD']['downpayment']=9000000 #this way u can update
print(company['bmw']['emi']) #this give you that value those you need through dict

for k,v in company.items():
    #print(k,v) #this give u all data in dict
    print(k,v['emi'],v['downpayment']) #this give u only that data those u need  in dict iterate
