f = open('book.txt','r')
dic = {}
ordereddic = {}
l = []
for line in f:
    line = line.strip()
    lis = line.split()
    for x in lis:
        while x[-1].isalpha() == False and len(x)>1: # removing trailing commas, full stops, etc.
            x = x[:-1]
        while x[0].isalpha() == False and len(x)>1: # removing leading commas, full stops, etc.
            x = x[1:]
        if len(x) == 1 and x.isalpha() == False:
            continue
        l.append(x)
f.close()

# adding to word dictionary 
for x in l: 
    if x in dic.keys():
        dic[x] = dic[x] + 1
    else:
        dic[x] = 1

# to print count in a ordered column
length = 0 
for key in dic.keys():
    if len(key) > length:
        length = len(key)

#to print words and counts in order of highest value
print('\033[4mWORD -- COUNT\033[0m')
usedkeys = [] #to prevent printing words twice
print_count = 0
for x in range(len(dic)):
    max = 0
    currentkey = ''
    
    for key,value in dic.items():
        if value > max and key not in usedkeys:
            max = value
            currentkey = key
    usedkeys.append(currentkey)
    print(f'{currentkey}',' '*(length-len(currentkey)),f' --   {max}')
    print_count += 1
    if print_count == 10: # to stop after printing top 10
        break

# #printing words and counts
# print('\033[4mWORD -- COUNT\033[0m')
# for key,value in dic.items():
#     print(f'{key}',' '*(length-len(key)),f' --   {value}')
