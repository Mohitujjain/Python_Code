#JSON:--
'''
-->json(java script object notation).
-->It is mainly used for storing and transferring data between the browser and the server.
-->json is text, written with javascript object notation.
-->python too supports json with a built-in package called json.
import json

json supports mainly 6 data types:
1. string
2. number
3. boolean
4. null
5. object
6. array

In python,json exists as a string.for example:
p='{"name":"Ms","comp":["BMW","Bugatti"]}'


blog={'URL':'www.volcanoms.com','name':'ms'}
to_json=json.dumps(blog)

'''

import json
d={
    'company_name':'Tata',
    'price':4500000
}
f=json.dumps(d)

print(type(f))

print(f)

#Converting json to python objects:-
# if you have a json string, you can parse it by using the json.loads() method.
d='{"cname":"BMW","fees":12000,"duration":"2 Months"}'   #json data
# d='[{"cname":"BMW","fees":12000,"duration":"2 Months"}]' this give u list
x=json.loads(d)

print(type(x))
print(x)

for a in x:
    print(a)  #if u need value write print(a,x[a])

#Writing & Reading JSON File
import json
file=open("posts.json" ,"r" )
x=file.read()
finaldata=json.loads(x)

print(finaldata);

for a in finaldata:
    print(a)   #2nd ,this give you each dict in seperate mode

for a in finaldata:
    print(a['title'],a['userID'])  #3rd this give u direct what u want in that


