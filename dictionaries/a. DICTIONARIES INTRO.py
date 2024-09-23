#DICTIONARIES
'''
key: the name given to a defined value in the dictionary
value: the defenition given to a key, a value you can call upon using the key
item: a key value pair
'''
#creating a dictionary (use {} brackets)
dic = {}
dic2 = dict({})

print(dic)

print('\n')

#to add a key value pair
dic['my age'] = 17
print(dic['my age'])
 
dic['my name'] = 'ahmed'
print(dic['my name'])

print('\n')

#to find num of items in a dictionary
print('length of dictionary:',len(dic))
print('\n')

#to print keys in dictionary:
for key in dic: # or for key in dic.keys():
    print(key)
#for values:
for value in dic.values():
    print(value)
print('\n')

for key,value in dic.items(): # prints key value pairs (item)
    print(key, '--', value)
